
from django.http import HttpResponse
from django.shortcuts import render

from .models import Star, Planet, Satellite, Resident
from .forms import StarForm, PlanetForm, SatelliteForm, ResidentForm


def get_planet(request):
    planets = Planet.objects.all()
    if planet_name := request.GET.get('planet_name'):
        planets = planets.filter(name=planet_name.capitalize())

    if star_name := request.GET.get('star_name'):
        planets = planets.objects.get_planet_name_by_star_name(star_name)

    if request.GET.get('is_habitable') is not None:
        planets = planets.not_habitable()
    else:
        planets = planets.habitable()

    return render(request, 'index.html', {"iterable": planets, "object": "Planets"})


def get_star(request):
    stars = Star.objects.all()
    if star_name := request.GET.get('star_name'):
        stars = stars.filter(name=star_name.capitalize())

    return render(request, 'index.html', {"iterable": stars, "object": "Stars"})


def get_satellite(request):
    satellites = Satellite.objects.all()
    if planet_name := request.GET.get('planet_name'):
        satellites = satellites.get_satellites_by_planet_name(planet_name)

    if request.GET.get('is_habitable') is not None:
        satellites = satellites.not_habitable()
    else:
        satellites = satellites.habitable()

    return render(request, 'index.html', {"iterable": satellites, "object": "Satellites"})


def get_resident(request):
    residents = Resident.objects.all()
    if planet_name := request.GET.get('planet_name'):
        residents = residents.get_residents_by_planet_name(planet_name)

    return render(request, 'index.html', {"iterable": residents, "object": "Residents"})


def add_model(request, given_form, given_url, name):

    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'index2.html', {'form': given_form(), 'given_url': given_url})


def add_star(request):
    return add_model(request, StarForm, 'add_star', 'star')


def add_planet(request):
    return add_model(request, PlanetForm, 'add_planet', 'planet')


def add_satellite(request):
    return add_model(request, SatelliteForm, 'add_satellite', 'satellite')


def add_resident(request):
    return add_model(request, ResidentForm, 'add_resident', 'resident')
