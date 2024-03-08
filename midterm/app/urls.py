from django.contrib import admin
from django.urls import path, include

from .views import get_room, get_hotel, add_room, add_customer, add_reservation, logout_view, login_view, register_view

urlpatterns = [
    path('get_room/', get_room, name='get_room',),
    path('get_hotel/', get_hotel, name='get_hotel'),
    path('add_room/', add_room, name='add_room'),
    path('add_customer/', add_customer, name='add_customer'),
    path('add_reservation/', add_reservation, name='add_reservation'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]