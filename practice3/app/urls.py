from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name='index'),
    path("cars/", add_car, name='cars')
]