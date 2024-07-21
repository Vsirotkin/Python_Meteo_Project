# weather/views.py
import json
from django.shortcuts import render
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
from .utils import fetch_weather_data


def welcome(request):
    return render(request, "weather/welcome.html")


@login_required
def home(request):
    with open('weather/cities.json', 'r') as file:
        cities = json.load(file)
    
    city_names = [city['name'] for city in cities]
    latitudes = [city['latitude'] for city in cities]
    longitudes = [city['longitude'] for city in cities]
    weather_data = fetch_weather_data(latitudes, longitudes)
    combined_data = list(zip(city_names, weather_data))

    selected_city = request.GET.get('city')
    if selected_city and selected_city != 'All Cities':
        combined_data = [(name, data) for name, data in combined_data if name == selected_city]
        # Store the last viewed city in the cache
        cache.set(f'last_viewed_city_{request.user.id}', selected_city)
    else:
        # Retrieve the last viewed city from the cache
        last_viewed_city = cache.get(f'last_viewed_city_{request.user.id}')
        if last_viewed_city:
            combined_data = [(name, data) for name, data in combined_data if name == last_viewed_city]

    return render(request, 'weather/home.html', {'combined_data': combined_data, 'city_names': city_names})
