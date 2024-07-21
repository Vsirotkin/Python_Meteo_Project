# weather/tests.py
"""
### Explanation

1. **HomeViewTestCase**:
   - Tests the `home` view with a selected city and without a selected city.
   - Uses mocking to simulate the behavior of `fetch_weather_data` and `cache`.

2. **WelcomeViewTestCase**:
   - Tests the `welcome` view to ensure it renders correctly and contains all city names from the JSON file.

3. **SearchCityViewTestCase**:
   - Tests the `search_city` view with a specified city and without a specified city.
   - Uses mocking to simulate the behavior of `fetch_weather_data`.

These tests cover the basic functionality of each view and ensure that they handle different scenarios correctly. You can expand these tests to cover more edge cases and specific behaviors as needed.

"""


from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from unittest.mock import patch
import json


### Test Cases for 'home' View
class HomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.client.login(username="testuser", password="12345")

    @patch("weather.views.fetch_weather_data")
    @patch("weather.views.cache")
    def test_home_view_with_selected_city(self, mock_cache, mock_fetch_weather_data):
        mock_fetch_weather_data.return_value = [{"temperature": 20}]
        with open("weather/cities.json", "r") as file:
            cities = json.load(file)
        city_names = [city["name"] for city in cities]
        selected_city = city_names[0]
        response = self.client.get(reverse("weather:home"), {"city": selected_city})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, selected_city)
        mock_cache.set.assert_called_once_with(
            f"last_viewed_city_{self.user.id}", selected_city
        )

    @patch("weather.views.fetch_weather_data")
    @patch("weather.views.cache")
    def test_home_view_with_no_selected_city(self, mock_cache, mock_fetch_weather_data):
        mock_fetch_weather_data.return_value = [{"temperature": 20}]
        response = self.client.get(reverse("weather:home"))
        self.assertEqual(response.status_code, 200)
        mock_cache.get.assert_called_once_with(f"last_viewed_city_{self.user.id}")


### Test Cases for `welcome` View
class WelcomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_welcome_view(self):
        with open("weather/cities.json", "r") as file:
            cities = json.load(file)
        city_names = [city["name"] for city in cities]
        response = self.client.get(reverse("weather:welcome"))
        self.assertEqual(response.status_code, 200)
        for city_name in city_names:
            self.assertContains(response, city_name)
    
    def test_welcome_view(self):
        with open('weather/cities.json', 'r') as file:
            cities = json.load(file)
        city_names = [city["name"] for city in cities]
        response = self.client.get(reverse('weather:welcome'))
        print(response.content)  # This will print the response content
        self.assertEqual(response.status_code, 200)
        for city_name in city_names:
            self.assertContains(response, city_name)


### Test Cases for `search_city` View
class SearchCityViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    @patch("weather.views.fetch_weather_data")
    def test_search_city_view_with_city(self, mock_fetch_weather_data):
        mock_fetch_weather_data.return_value = [{"temperature": 20}]
        with open("weather/cities.json", "r") as file:
            cities = json.load(file)
        city_names = [city["name"] for city in cities]
        selected_city = city_names[0]
        response = self.client.get(reverse("weather:search_city"), {"city": selected_city})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, selected_city)
    
    @patch("weather.views.fetch_weather_data")
    def test_search_city_view_with_no_city(self, mock_fetch_weather_data):
        mock_fetch_weather_data.return_value = [{"temperature": 20}]
        response = self.client.get(reverse("weather:search_city"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No data available for the selected city.")
