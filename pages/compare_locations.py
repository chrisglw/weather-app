import streamlit as st
import polars as pl
from utils.weather_api import fetch_weather
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def fetch_multiple_cities(start_date, end_date):
    locations = {
        "BYU Idaho": {"lat": 43.8145, "lon": -111.7833},
        "BYU Hawaii": {"lat": 21.6419, "lon": -157.9267},
        "BYU Provo": {"lat": 40.25, "lon": -111.65}
    }
    city_data = {}
    for city, coords in locations.items():
        try:
            df = fetch_weather(coords, start_date, end_date)
            city_data[city] = df.rename({"temperature_2m": city})
        except Exception as e:
            st.error(f"Failed to fetch data for {city}: {e}")

    combined_df = city_data[list(city_data.keys())[0]].select("datetime")
    for city, data in city_data.items():
        combined_df = pl.concat([combined_df, data.select(city)], how="horizontal")
    return combined_df

def display_visualizations(df):
    st.subheader("Daily High Temperatures Across Cities")
    melted_df = df.melt(id_vars=["datetime"], variable_name="City", value_name="Temperature")
    
    plt.figure(figsize=(10, 6))
    for city in df.columns[1:]:
        plt.plot(df["datetime"], df[city], label=city)
    plt.xlabel("Datetime")
    plt.ylabel("Temperature (°F)")
    plt.title("Temperature Comparison")
    plt.legend()
    st.pyplot(plt)

def calculate_kpis(df):
    kpis = {}
    for city in df.columns[1:]:
        highest = df[city].max()
        lowest = df[city].min()
        kpis[city] = (highest, lowest)
    return kpis

def main():
    st.title("Compare Weather Data for All BYU Locations 🌍")
    st.sidebar.header("User Input")
    start_date = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=15))
    end_date = st.sidebar.date_input("End Date", datetime.now())

    if start_date and end_date:
        st.write("Fetching weather data for all BYU locations...")
        try:
            combined_data = fetch_multiple_cities(start_date, end_date)
            st.dataframe(combined_data)

            st.subheader("Key Performance Indicators (KPIs)")
            kpis = calculate_kpis(combined_data)
            for city, (highest, lowest) in kpis.items():
                st.write(f"**{city}:** Highest Temp: {highest:.2f} °F | Lowest Temp: {lowest:.2f} °F")

            display_visualizations(combined_data)
        except Exception as e:
            st.error(f"Error: {e}")
