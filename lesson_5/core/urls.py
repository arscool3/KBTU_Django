from django.urls import path

from core.views import get_country_by_name, get_cities, get_citizens

urlpatterns = [
    path("countries/", get_country_by_name),
    path("cities/", get_cities),
    path("citizens/", get_citizens),
]