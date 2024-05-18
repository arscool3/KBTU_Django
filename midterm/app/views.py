from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .filters import RoomFilter

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, decorators, logout, forms

from .forms import CustomerForm, RoomForm, ReservationForm
from .models import Hotel, Room, Reservation, Customer
from .serializers import HotelSerializer, RoomSerializer, CustomerSerializer, ReservationSerializer



class HotelViewSet(ModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']

class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = RoomFilter

class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()

class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        reservation = serializer.save()
        room = reservation.room
        room.available = False
        room.save()


@decorators.login_required(login_url='login')
def get_hotel(request):
    hotels = Hotel.objects.all()
    if hotel_name := request.GET.get('hotel_name'):
        hotels = hotels.filter_by_name(hotel_name)

    return render(request, 'index.html', {"iterable": hotels, "object": "Hotels"})


@decorators.login_required(login_url='login')
def get_room(request):
    rooms = Room.objects.all()
    if room_name := request.GET.get('room_name'):
        rooms = rooms.filter(name=room_name.capitalize())

    if hotel_name := request.GET.get('hotel_name'):
        rooms = rooms.get_rooms_by_hotel_name(hotel_name)

    if type_name := request.GET.get('type_name'):
        rooms = rooms.get_rooms_by_type(type_name)

    if request.GET.get('is_available') is not None:
        rooms = rooms.not_available()
    else:
        rooms = rooms.available()

    return render(request, 'index.html', {"iterable": rooms, "object": "Rooms"})


def add_model(request, given_form, given_url, name):

    if request.method == "POST":
        form = given_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, {name} was created')

    return render(request, 'index2.html', {'form': given_form(), 'given_url': given_url})


@decorators.permission_required('core.can_add_customer', login_url='login')
def add_customer(request):
    return add_model(request, CustomerForm, 'add_customer', 'customer')


def add_room(request):
    return add_model(request, RoomForm, 'add_room', 'room')


def add_reservation(request):
    form = ReservationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            reservation = form.save()
            room = reservation.room
            room.available = False
            room.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, Reservation was created')

    return render(request, 'index2.html', {'form': ReservationForm, 'given_url': 'add_reservation'})


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return HttpResponse("everything is ok")
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index2.html', {'form': forms.AuthenticationForm()})


def logout_view(request):
    logout(request)
    return HttpResponse("You have logout")


def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index2.html', {'form': given_form()})


def register_view(request):
    return basic_form(request, forms.UserCreationForm)
