from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('forms/country', views.countryForm, name="countryForm"),
    path('forms/city', views.cityForm, name="cityForm"),
    path('forms/citizen', views.citizenForm, name="citizenForm"),
    path('forms/president', views.presidentForm, name="presidentForm"),
    path('views/countries', views.countries, name="countries"),
    path('views/countries/<int:order>', views.countries, name="countries"),
    path('views/cities', views.cities, name="cities"),
    path('views/citizens', views.citizens, name="citizens"),
    path('views/adults', views.adults, name="adults"),
    path('views/children', views.children, name="children"),
    path('views/presidents', views.presidents, name="presidents"),
    path('views/country/<str:name>', views.country, name="country"),
    path('views/city/<str:name>', views.city, name="city"),
    path('views/citizen/<str:name>', views.citizen, name="citizen"),
    path('views/president/<str:name>', views.president, name="president"),
]