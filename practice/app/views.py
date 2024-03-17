from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def contact(request):
    return HttpResponse("Contact us at example@example.com")

def about(request):
    return HttpResponse("This is the about page!")

def home(request):
    return HttpResponse("Welcome to the home page!")