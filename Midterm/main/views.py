import dataclasses
from rest_framework.views import APIView
from .serializers import FlightDimSerializer
from django.http import Http404, JsonResponse

from django.shortcuts import render, HttpResponse, redirect
from .models import Airline, Aircraft, City, Airport, Flight_fact, Flight_dim
from collections import defaultdict
from .forms import TicketSearchForm, FlightForm
from django.contrib.auth import authenticate, login, decorators, logout, forms
import json

def format_time(time):
    # Format time using strftime
    formatted_time = time.strftime('%H:%M')
    return formatted_time

def entry_page(request):
    return render(request, 'entry_page.html')

def admin_view(request):
    return render(request, 'admin.html')


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

            flights = flights.all().order_by('flight_code__dept_time')

            flight_detail = {
                'From': airport_from.name,
                'To': airport_to.name,
                'Flight_date': flight_date,
                'Seat_Class': seat_class,
            }
            serialized_flights = []
            for flight in flights:
                serialized_flight = {
                    'flight_id': flight.flight_id,
                    'flight_code': flight.flight_code.flight_code,
                    'airline_name': flight.flight_code.airline_name.airline_name,
                    'dept_time': flight.flight_code.dept_time,
                    'arr_time': flight.flight_code.arr_time
                }
                serialized_flights.append(serialized_flight)

            print(serialized_flights)
            return render(request, 'flight_option.html', {'flights': serialized_flights, 'flight_detail': flight_detail, 'header':'Flights by filter'})
            #return JsonResponse({'flights': serialized_flights, 'flight_detail': flight_detail, 'header':'Flights by filter'})
    elif request.method == "GET":
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

def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('entry_page')
        else:
            raise Exception(f"some erros {form.errors}")
    elif request.method == "GET":
        return render(request, 'log_reg.html', {'form': given_form()})


def register_view(request):
    return basic_form(request, forms.UserCreationForm)

def logout_view(request):
    logout(request)
    return redirect('entry_page')

def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if user.is_superuser:
                    #return redirect('admin:index')
                    return redirect('admin_page')
                return redirect('search_ticket')
            except Exception:
                pass
        else:
            return render(request, 'log_reg.html', {'form': forms.AuthenticationForm(), 'comment': 'Wrong credentials, or you still do not have access to enter the Web page'})
    elif request.method == "GET":
        return render(request, 'log_reg.html', {'form': forms.AuthenticationForm()})

def aircraft_time_scheduling(request):
    form = FlightForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        flight_code = form.cleaned_data['Flight']
        flight_date = form.cleaned_data['Date']

        flight_fact = Flight_fact.objects
        data = flight_fact.filter(flight_code=flight_code).values('dept_time', 'arr_time').first()
        print(data)
        data = {k: str(v) for k, v in data.items()}
        print(data)
        data = {'dept_arr_times': data, 'date': str(flight_date)}
        print(data)
        return render(request, 'aircraft_time_scheduling.html', {'form': form, 'data': json.dumps(data), 'header': 'Choose the aircraft operating the flight'})
    elif request.method == "GET":
        return render(request, 'aircraft_time_scheduling.html', {'form': form, 'header': 'Choose flight to process'})

class AircraftByFlightIdView(APIView):
    def get(self, request):
        flight_id = request.query_params.get('id')
        try:
            flight_dim = Flight_dim.objects.get(flight_id=flight_id)
            serializer = FlightDimSerializer(flight_dim)
            if serializer.data['aircraft']:
                return JsonResponse({'aircraft_full_name': serializer.data['aircraft']['full_name']})
            else:
                return JsonResponse({'aircraft_full_name': 'Aircraft do not assigned yet'})
        except Flight_dim.DoesNotExist:
            raise Http404('Flight does not exist')
