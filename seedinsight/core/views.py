# Create your views here.
from django.shortcuts import render
from .models import Seed, Ecozone

def home(request):
    return render(request, 'core/home.html')

def seed_recommendation(request):
    seeds = None
    if request.method == 'POST':
        ecozone_id = request.POST.get('ecozone')
        ecozone = Ecozone.objects.get(id=ecozone_id)
        seeds = Seed.objects.filter(ecozone=ecozone)
    return render(request, 'core/recommendation.html', {'seeds': seeds})

