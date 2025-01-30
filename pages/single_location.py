import streamlit as st
from utils.weather_api import fetch_weather
from datetime import datetime, timedelta

def main():
    st.title("Weather Dashboard for Single BYU Location 🌤️")

    locations = {
        "BYU Idaho": {"lat": 43.8145, "lon": -111.7833},
        "BYU Hawaii": {"lat": 21.6419, "lon": -157.9267},
        "BYU Provo": {"lat": 40.25, "lon": -111.65}
    }

    st.sidebar.header("User Input")
    selected_city = st.sidebar.selectbox("Select a BYU Location", list(locations.keys()))
    start_date = st.sidebar.date_input("Start Date", datetime.now() - timedelta(days=15))
    end_date = st.sidebar.date_input("End Date", datetime.now())

    if start_date and end_date:
        try:
            weather_data = fetch_weather(locations[selected_city], start_date, end_date)
            st.write(f"Weather Data for **{selected_city}**")
            st.dataframe(weather_data)
        except Exception as e:
            st.error(f"Error fetching data: {e}")
