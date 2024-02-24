# views.py

from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the homepage!")

def about(request):
    return HttpResponse("This is the about page.")

def next(request):
    return HttpResponse("This is the next page.")
