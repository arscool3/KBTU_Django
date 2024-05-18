from django.contrib import admin
from django.urls import path
from .views import get_star,get_planet, get_resident, get_satellite, add_star, add_planet, add_resident, add_satellite

urlpatterns = [
    path('star/', get_star),
    path('planet/', get_planet),
    path('resident/', get_resident),
    path('satellite/', get_satellite),
    path('add_star/', add_star, name='add_star'),
    path('add_planet/', add_planet, name='add_planet'),
    path('add_resident/',  add_resident, name='add_resident'),
    path('add_satellite/', add_satellite, name='add_satellite')
]
