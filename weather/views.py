from django.shortcuts import render

def home(request):
    cities = ['New York', 'Berlin', 'Moscow', 'Nizhny Novgorod']
    return render(request, 'weather/home.html', {'cities': cities})
