import requests
import polars as pl

def fetch_weather(location, start_date, end_date, variable="temperature_2m", timezone="America/Denver"):
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": location['lat'],
        "longitude": location['lon'],
        "start_date": start_date,
        "end_date": end_date,
        "hourly": variable,
        "timezone": timezone
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        hourly_data = data['hourly']
        
        if variable == "temperature_2m":
            df = pl.DataFrame({
                "datetime": hourly_data['time'],
                variable: [temp * 9 / 5 + 32 for temp in hourly_data[variable]]
            })
        else:
            df = pl.DataFrame({
                "datetime": hourly_data['time'],
                variable: hourly_data[variable]
            })
        return df
    else:
        raise Exception(f"API request failed: {response.status_code}")
