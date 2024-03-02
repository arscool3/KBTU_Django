import dataclasses

from django.http import HttpResponse
from django.shortcuts import render
from .models import Airline, Aircraft, City, Airport, Flight_fact, Flight_dim

def view(request):
    return render(request, 'index.html')


