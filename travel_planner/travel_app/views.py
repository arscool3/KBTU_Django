# travel_app/views.py
from django.shortcuts import render
from .models import Destination, Itinerary, Activity, Review

def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'destination_list.html', {'destinations': destinations})

def destination_detail(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    return render(request, 'destination_detail.html', {'destination': destination})

# Add similar views for Itineraries, Activities, User profiles, and Reviews
