
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from core.models import Country, City, Citizen


# Django ORM is lazy

def get_country_by_name(request):
    countries = Country.objects.get_kaz().get_name(3)
    # if name := request.GET.get('name'):
    #     countries = countries.filter(name=name.capitalize())
    # countries = countries.all()
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
