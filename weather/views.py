import json
from django.shortcuts import render
from .utils import fetch_weather_data

def home(request):
    with open('weather/cities.json', 'r') as file:
        cities = json.load(file)
    
    latitudes = [city['latitude'] for city in cities]
    longitudes = [city['longitude'] for city in cities]
    city_names = [city['name'] for city in cities]
    
    weather_data = fetch_weather_data(latitudes, longitudes)
    combined_data = list(zip(city_names, weather_data))
    return render(request, 'weather/home.html', {'combined_data': combined_data})