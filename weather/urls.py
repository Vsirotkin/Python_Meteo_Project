from django.urls import path
from . import views


app_name = "weather"

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("home/", views.home, name="home"),
    path('search/', views.search_city, name='search_city'),
    path('autocomplete/', views.autocomplete_city, name='autocomplete_city'),
]

# API
urlpatterns += [
    path(
        "api/search-history/", views.SearchHistoryAPIView.as_view(), name="search-history-api"
    ),
]
