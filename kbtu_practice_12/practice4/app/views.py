
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from app.models import Country, City, Citizen


# Django ORM is lazy

def get_country_by_name(request):
    countries = Country.objects
    if name := request.GET.get('name'):
        countries = countries.filter(name=name.capitalize())
    countries = countries.all()
    return render(request, "index.html", {"iterable": countries, "object": "Countries"})


def get_cities(request):
    cities = City.objects
    if country_name := request.GET.get('country_name'):
        cities = cities.filter(country__name=country_name.capitalize())
    cities = cities.all()
    return render(request, 'index.html', {"iterable": cities, "object": "Cities"})


def get_citizens(request):
    citizens = Citizen.objects
    if country_name := request.GET.get('country_name'):
        citizens = citizens.filter(
            Q(country__name=country_name.capitalize()) | Q(country__name=country_name.upper()) | Q(country__name=country_name.lower())
        )

    if age := request.GET.get('age'):
        citizens = citizens.filter(
            age=age
        )
    if request.GET.get('is_criminal') is not None:
        citizens = citizens.criminals()
    else:
        citizens = citizens.not_criminals()

    citizens = citizens.all()

    return render(request, 'index.html', {"iterable": citizens, "object": "Citizens"})

from django.shortcuts import render, redirect
from .forms import CountryForm, CitizenForm

def create_country(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            countries = Country.objects
            countries = countries.all()
            return render(request, 'index.html', {"iterable": countries, "object": "Countries"})  
    else:
        form = CountryForm()
    return render(request, 'create_country.html', {'form': form})

def create_citizen(request):
    if request.method == 'POST':
        form = CitizenForm(request.POST)
        if form.is_valid():
            form.save()
            citizens = Citizen.objects
            citizens = citizens.all()
            return render(request, 'index.html', {"iterable": citizens, "object": "Citizens"}) 
    else:
        form = CitizenForm()
    return render(request, 'create_citizen.html', {'form': form})