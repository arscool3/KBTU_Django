from django.db.models import Q
from django.shortcuts import render, HttpResponse
from werkzeug.utils import redirect
from core.serializers import CountrySerializer, CitySerializer, CitizenSerializer, CarSerializer
from core.forms import LoginForm
from django.contrib.auth import authenticate, login, decorators, logout
from rest_framework.response import Response
from core.models import Country, City, Citizen, Car
from rest_framework.decorators import api_view


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            login(request, user)
            if next := request.GET.get('next'):
                return redirect(next)
            return HttpResponse('Logged in successfully!')
        else:
            raise Exception('some errors')
    return render(request, 'index.html', {'form': LoginForm()})


def logout_view(request):
    logout(request)
    return redirect('login')


@decorators.login_required(login_url='login')
def check_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f'{request.user} is authenticated!')
    return Exception(f'{request.user} is not authenticated!')


def add(request):
    pass


@api_view(['GET'])
def get_country_by_name(request):
    countries = Country.objects
    if name := request.GET.get('name'):
        countries = countries.filter(name=name.capitalize())
    countries = countries.all()
    return Response(CountrySerializer(countries, many=True).data, status=200, template_name='index.html')


@api_view(['GET'])
def get_cities(request):
    cities = City.objects
    if country_name := request.GET.get('country_name'):
        cities = cities.filter(Q(country__name=country_name.capitalize()) | Q(country__name=country_name.upper()) | Q(
            country__name=country_name.lower())
                               )
    cities = cities.all()
    return Response(CitySerializer(cities, many=True).data, status=200, template_name='index.html')


@api_view(['GET'])
def get_citizens(request):
    citizens = Citizen.objects
    if country_name := request.GET.get('country_name'):
        citizens = citizens.filter(
            Q(country__name=country_name.capitalize()) | Q(country__name=country_name.upper()) | Q(
                country__name=country_name.lower())
            )

    if age := request.GET.get('age'):
        citizens = citizens.filter(
            age=age
        )

    if is_criminal := request.GET.get('is_criminal') is not None:
        citizens = citizens.criminals()
    else:
        citizens = citizens.not_criminals()
    if is_licenced := request.GET.get('is_licenced') is None:
        citizens = citizens.licence()
    else:
        citizens = citizens.not_licence()

    citizens = citizens.all()
    return Response(CitizenSerializer(citizens, many=True).data, status=200, template_name='index.html')


@api_view(['GET'])
def get_cars(request):
    cars = Car.objects
    if country_name := request.GET.get('country_name'):
        cars = cars.filter(Q(country__name=country_name.capitalize()) | Q(country__name=country_name.upper()) | Q(
            country__name=country_name.lower())
                           )

    if citizen := request.GET.get('citizen_name'):
        cars = cars.filter(Q(citizen__name=citizen.capitalize()) | Q(citizen__name=citizen.upper()) | Q(
            citizen__name=citizen.lower())
                           )

    if year := request.GET.get('year'):
        cars = cars.filter(
            year=year
        )

    if is_active := request.GET.get('is_active') is None:
        cars = cars.active()
    else:
        cars = cars.not_active()

    cars = cars.all()
    return Response(CarSerializer(cars, many=True).data, status=200, template_name='index.html')


@api_view(['GET'])
def get_only_new_cars(request):
    cars = Car.objects.get_only_new_cars()
    return Response(CarSerializer(cars, many=True).data, status=200, template_name='index.html')


@api_view(['GET'])
def get_only_german_cars(request):
    cars = Car.objects.get_only_german_cars()
    return Response(CarSerializer(cars, many=True).data, status=200, template_name='index.html')


@api_view(['GET'])
def get_only_usa_cars(request):
    cars = Car.objects.get_only_usa_cars()
    return Response(CarSerializer(cars, many=True).data, status=200, template_name='index.html')
