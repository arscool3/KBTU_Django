# travel_app/urls.py
from django.urls import path
from .views import destination_list, destination_detail

urlpatterns = [
    path('destinations/', destination_list, name='destination_list'),
    path('destinations/<int:destination_id>/', destination_detail, name='destination_detail'),
    # Add similar paths for Itineraries, Activities, User profiles, and Reviews
]
