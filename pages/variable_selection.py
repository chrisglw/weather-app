import streamlit as st
import polars as pl
from datetime import datetime, timedelta
from utils.weather_api import fetch_weather
import matplotlib.pyplot as plt

def main():
    st.title("Compare Multiple Weather Variables Across BYU Locations 🌤️")
    
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
    
    def fetch_all_variables(location, start_date, end_date, timezone_selection):
        dataframes = {}
        for label, variable in weather_variables.items():
            try:
                df = fetch_weather(location, start_date, end_date, variable, timezone_selection)
                df = df.rename({variable: label})
                dataframes[label] = df
            except Exception as e:
                st.error(f"Error fetching {label} data: {e}")
        return dataframes
    
    st.sidebar.header("User Input")
    start_date = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=15))
    end_date = st.sidebar.date_input("End Date", datetime.now())
    timezone_selection = st.sidebar.radio("Select Time Zone", ["America/Denver", "Pacific/Honolulu"])
    
    if start_date and end_date:
        st.write("Fetching all weather variables for each BYU location...")
        all_data = {}
        for city, coords in locations.items():
            st.write(f"Fetching data for **{city}**...")
            all_data[city] = fetch_all_variables(coords, start_date, end_date, timezone_selection)
        
        st.subheader("Combined Weather Data Across Cities and Variables")
        for city, dataframes in all_data.items():
            st.write(f"**{city}**")
            
            datetime_df = dataframes[list(dataframes.keys())[0]].select("datetime")
            data_without_datetime = [df.drop("datetime") for df in dataframes.values()]
            combined_df = pl.concat([datetime_df] + data_without_datetime, how="horizontal")

            st.dataframe(combined_df)
            
            st.subheader(f"Visualizing Weather Variables for {city}")
            plt.figure(figsize=(10, 6))
            for label in dataframes:
                plt.plot(combined_df["datetime"], combined_df[label], label=label)
            plt.xlabel("Datetime")
            plt.ylabel("Values")
            plt.title(f"Weather Variables for {city}")
            plt.legend()
            st.pyplot(plt)
        
        st.subheader("Boxplot of Weather Variables Across All Cities")
        plt.figure(figsize=(12, 8))

        for i, city in enumerate(all_data.keys(), start=1):
            city_data = all_data[city]
            
            data_without_datetime = [df.drop("datetime") for df in city_data.values()]
            combined_city_df = pl.concat(data_without_datetime, how="horizontal").to_pandas()
            
            plt.boxplot(combined_city_df.values,
                        labels=combined_city_df.columns,
                        positions=[i + idx * 0.3 for idx in range(len(weather_variables))],
                        widths=0.25)

        plt.title("Weather Variable Comparison")
        plt.ylabel("Values")
        plt.xticks(range(1, len(all_data.keys()) + 1), all_data.keys())
        plt.grid(True)
        st.pyplot(plt)

if __name__ == "__main__":
    main()
