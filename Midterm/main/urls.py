from django.urls import path

from .views import get_flights, search_ticket

urlpatterns = [
    path("get_flights/", get_flights),
    path("", search_ticket)
]