# views.py
import json
from django.shortcuts import render
from .utils import fetch_weather_data

def home(request):
    with open('weather/cities.json', 'r') as file:
        cities = json.load(file)
    
    city_names = [city['name'] for city in cities]
    latitudes = [city['latitude'] for city in cities]
    longitudes = [city['longitude'] for city in cities]
    weather_data = fetch_weather_data(latitudes, longitudes)
    combined_data = list(zip(city_names, weather_data))

    selected_city = request.GET.get('city')
    if selected_city:
        combined_data = [(name, data) for name, data in combined_data if name == selected_city]

    return render(request, 'weather/home.html', {'combined_data': combined_data, 'city_names': city_names})