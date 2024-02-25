from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("countries/", get_country_by_name),
    path("cities/", get_cities),
    path("citizens/", get_citizens),
    path("createcountry", create_country),
    path("create_citizen", create_citizen)
]