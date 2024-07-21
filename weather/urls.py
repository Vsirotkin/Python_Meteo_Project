from django.urls import path
from . import views

app_name = "weather"

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("home/", views.home, name="home"),
]
