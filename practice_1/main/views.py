from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my Django project!")

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("Contact us at example@example.com")

