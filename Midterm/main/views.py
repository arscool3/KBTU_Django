import dataclasses

from django.http import HttpResponse
from django.shortcuts import render
from .models import Airline, Aircraft, City, Airport, Flight_fact, Flight_dim
from collections import defaultdict
from .forms import TicketSearchForm

def search_ticket(request):
    if request.method == "POST":
        form = TicketSearchForm(request.POST)
        if form.is_valid():
            airport_from = form.cleaned_data["From"]
            airport_to = form.cleaned_data["To"]
            flight_date = form.cleaned_data["Flight_date"]
            seat_class = form.cleaned_data["Seat_Class"]
            print(airport_from, airport_to, flight_date, seat_class)

            flights = Flight_dim.objects
            flights = flights.get_flight_by_filter(airport_from, airport_to, flight_date)

            flights = flights.all().order_by('flight_date', 'flight_code__dept_time')

            grouped_flights = defaultdict(list)
            for flight in flights:
                grouped_flights[flight.dept_date()].append(flight)

            return render(request, 'index.html', {'grouped_flights': dict(grouped_flights), 'header':'Flights by filter'})
    else:
        form = TicketSearchForm()
        return render(request, 'index2.html', {'form': form})

def get_flights(request):
    flights = Flight_dim.objects
    if flight_code := request.GET.get('flight_code'):
        flights = flights.filter(flight_code__flight_code = flight_code)

    if dept_airport := request.GET.get('from'):
        flights = flights.filter(flight_code__airport_from__airport_code=dept_airport)

    if arr_airport := request.GET.get('to'):
        flights = flights.filter(flight_code__airport_to__airport_code=arr_airport)

    flights = flights.all().order_by('flight_date', 'flight_code__dept_time')

    grouped_flights = defaultdict(list)
    for flight in flights:
        grouped_flights[flight.dept_date()].append(flight)
    return render(request, 'index.html', {'grouped_flights': dict(grouped_flights), 'header':'Flights by filter'})


