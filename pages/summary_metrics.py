import streamlit as st
import polars as pl
from datetime import datetime, timedelta
from utils.weather_api import fetch_weather 

locations = {
    "BYU Idaho": {"lat": 43.8145, "lon": -111.7833},
    "BYU Hawaii": {"lat": 21.6419, "lon": -157.9267},
    "BYU Provo": {"lat": 40.25, "lon": -111.65}
}

weather_variables = {
    "Temperature (°F)": "temperature_2m",
    "Wind Speed (mph)": "windspeed_10m",
    "Relative Humidity (%)": "relative_humidity_2m"
}

def fetch_multiple_cities(start_date, end_date, variable, timezone_selection):
    city_data = {}
    for city, coords in locations.items():
        df = fetch_weather(coords, start_date, end_date, variable, timezone_selection)
        city_data[city] = df.rename({variable: city})
    combined_df = city_data[list(city_data.keys())[0]].select("datetime")
    for city, data in city_data.items():
        combined_df = pl.concat([combined_df, data.select(city)], how="horizontal")
    return combined_df

def calculate_summary_metrics(df):
    avg_values = df.select([pl.mean(city).alias(city) for city in df.columns if city != "datetime"])
    max_values = df.select([pl.max(city).alias(city) for city in df.columns if city != "datetime"])
    min_values = df.select([pl.min(city).alias(city) for city in df.columns if city != "datetime"])

    avg_summary = avg_values.row(0)
    max_summary = max_values.row(0)
    min_summary = min_values.row(0)
    return avg_summary, max_summary, min_summary

def main():
    st.title("Compare Weather Metrics Across BYU Locations 📊")
    
    st.sidebar.header("User Input")
    start_date = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=15))
    end_date = st.sidebar.date_input("End Date", datetime.now())
    selected_variable_label = st.sidebar.selectbox("Select Weather Variable", weather_variables.keys())
    timezone_selection = st.sidebar.radio("Select Time Zone", ["America/Denver", "Pacific/Honolulu"])
    selected_variable = weather_variables[selected_variable_label]
    
    if start_date and end_date:
        with st.spinner("Fetching weather data across all BYU locations..."):
            combined_data = fetch_multiple_cities(start_date, end_date, selected_variable, timezone_selection)
                
        st.write(f"### {selected_variable_label} Data Across Locations")
        st.dataframe(combined_data)
        
        avg_summary, max_summary, min_summary = calculate_summary_metrics(combined_data)

        st.subheader("Key Performance Indicators (KPIs)")
        kpi_cols = st.columns(len(locations))
        for idx, city in enumerate(locations):
            with kpi_cols[idx]:
                st.metric(f"{city} - Avg", f"{avg_summary[idx]:.2f}")
                st.metric(f"{city} - Max", f"{max_summary[idx]:.2f}")
                st.metric(f"{city} - Min", f"{min_summary[idx]:.2f}")

if __name__ == "__main__":
    main()
