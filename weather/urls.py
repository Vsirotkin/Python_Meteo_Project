from django.urls import path
from . import views

from .views import SearchHistoryAPIView

app_name = "weather"

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("home/", views.home, name="home"),
]

# API
urlpatterns += [
    path(
        "api/search-history/", SearchHistoryAPIView.as_view(), name="search-history-api"
    ),
]
