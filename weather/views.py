# myapp/views.py
from django.shortcuts import render
from .utils import fetch_weather_data

def home(request):
    latitudes = [52.52, 56.3287, 40.7143, 52.5244]  # Example latitudes
    longitudes = [13.41, 44.002, -74.006, 13.4105]  # Example longitudes
    city_names = ["Moscow", "Nizhny Novgorod", "New York", "Berlin"]
    weather_data = fetch_weather_data(latitudes, longitudes)
    combined_data = list(zip(city_names, weather_data))
    return render(request, 'weather/home.html', {'combined_data': combined_data})