# myapp/utils.py
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

def fetch_weather_data(latitudes, longitudes):
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # Make sure all required weather variables are listed here
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitudes,
        "longitude": longitudes,
        "daily": ["temperature_2m_max", "temperature_2m_min"],
        "timezone": "Europe/Moscow"
    }
    responses = openmeteo.weather_api(url, params=params)

    all_weather_data = []

    for response in responses:
        # print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
        # print(f"Elevation {response.Elevation()} m asl")
        # print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
        # print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

        # Process daily data. The order of variables needs to be the same as requested.
        daily = response.Daily()
        daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
        daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()

        daily_data = {"date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s", utc=True),
            end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left"
        )}
        daily_data["temperature_2m_max"] = [f"{temp:.1f}" for temp in daily_temperature_2m_max]
        daily_data["temperature_2m_min"] = [f"{temp:.1f}" for temp in daily_temperature_2m_min]

        daily_dataframe = pd.DataFrame(data=daily_data)
        print(daily_dataframe)

        all_weather_data.append(daily_dataframe.to_dict(orient="records"))

    return all_weather_data