from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Destination, Trip, Activity

def home(request):
    destinations = Destination.objects.all()
    return render(request, 'home.html', {'destinations': destinations})

def destination_detail(request, destination_id):
    destination = Destination.objects.get(id=destination_id)
    return render(request, 'destination_detail.html', {'destination': destination})

@login_required
def create_trip(request):
    if request.method == 'POST':
        # Process form data and create a new trip
        return redirect('home')
    return render(request, 'create_trip.html')

def trip_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    return render(request, 'trip_detail.html', {'trip': trip})

@login_required
def user_trips(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, 'user_trips.html', {'trips': trips})

# Additional views for creating, updating, and deleting trips and activities...

from django.http import HttpResponseForbidden
from .forms import TripForm, ActivityForm

@login_required
def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.user = request.user
            trip.save()
            return redirect('user_trips')
    else:
        form = TripForm()
    return render(request, 'create_trip.html', {'form': form})

@login_required
def update_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    if trip.user != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('trip_detail', trip_id=trip.id)
    else:
        form = TripForm(instance=trip)
    return render(request, 'update_trip.html', {'form': form, 'trip': trip})

@login_required
def delete_trip(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    if trip.user != request.user:
        return HttpResponseForbidden()
    trip.delete()
    return redirect('user_trips')

@login_required
def add_activity(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    if trip.user != request.user:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save(commit=False)
            activity.trip = trip
            activity.save()
            return redirect('trip_detail', trip_id=trip.id)
    else:
        form = ActivityForm()
    return render(request, 'add_activity.html', {'form': form, 'trip': trip})

@login_required
def remove_activity(request, activity_id):
    activity = Activity.objects.get(id=activity_id)
    trip_id = activity.trip.id
    if activity.trip.user != request.user:
        return HttpResponseForbidden()
    activity.delete()
    return redirect('trip_detail', trip_id=trip_id)

# views.py
from rest_framework import generics
from .models import Destination, Trip, Activity
from .serializers import DestinationSerializer, TripSerializer, ActivitySerializer

class DestinationList(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class DestinationDetail(generics.RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class TripList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

# views.py (example usage)
from .tasks import send_trip_notification_email

def create_trip(request):
    # Your logic to create a trip
    # After creating the trip, call the task
    send_trip_notification_email.send(trip_id=new_trip.id)
    # Rest of your view logic
