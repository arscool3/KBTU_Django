from django.db.models import Q
from django.shortcuts import render, HttpResponse
from werkzeug.utils import redirect
from core.serializers import CountrySerializer, CitySerializer, CitizenSerializer, CarSerializer
from rest_framework.decorators import action
from django.contrib.auth import decorators, logout
from rest_framework.response import Response
from core.models import Country, City, Citizen, Car
from rest_framework.decorators import api_view
from .forms import SignupForm
from rest_framework import viewsets
from .tasks import notify_new_citizen


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form': form
    })

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

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    @action(detail=False, methods=['get'])
    def largest_area(self, request):
        largest_country = self.queryset.order_by('-area').first()
        serializer = self.get_serializer(largest_country)
        return Response(serializer.data)


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CitizenViewSet(viewsets.ModelViewSet):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer

    def perform_create(self, serializer):
        citizen = serializer.save()
        notify_new_citizen.send(citizen.id)

    @action(detail=False, methods=['get'])
    def criminals(self, request):
        criminals = self.queryset.criminals()
        serializer = self.get_serializer(criminals, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def not_criminals(self, request):
        non_criminals = self.queryset.not_criminals()
        serializer = self.get_serializer(non_criminals, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def with_licence(self, request):
        with_licence = self.queryset.licence()
        serializer = self.get_serializer(with_licence, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def without_licence(self, request):
        without_licence = self.queryset.not_licence()
        serializer = self.get_serializer(without_licence, many=True)
        return Response(serializer.data)


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    @action(detail=False, methods=['get'])
    def active(self, request):
        active_cars = self.queryset.active()
        serializer = self.get_serializer(active_cars, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def not_active(self, request):
        not_active_cars = self.queryset.not_active()
        serializer = self.get_serializer(not_active_cars, many=True)
        return Response(serializer.data)

