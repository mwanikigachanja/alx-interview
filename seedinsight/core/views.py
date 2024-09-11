# Create your views here.
import requests
from django.shortcuts import render
from .models import Seed, Ecozone

def fetch_location_data():
    response = requests.get('https://ipapi.co/json/')
    return response.json()

def fetch_weather_data(location):
    apiKey = 'your_openweather_api_key'
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={apiKey}&units=metric')
    return response.json()

def home(request):
    return render(request, 'core/home.html')

def seed_recommendation(request):
    seeds = None
    if request.method == 'POST':
        ecozone_id = request.POST.get('ecozone')
        ecozone = Ecozone.objects.get(id=ecozone_id)
        seeds = Seed.objects.filter(ecozone=ecozone)
    return render(request, 'core/recommendation.html', {'seeds': seeds})

