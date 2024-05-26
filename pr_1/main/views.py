from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to my project")

def about(request):
    return HttpResponse("This is very simple kind of django project")

def contact(request):
    return HttpResponse("The owner is Zhadiger")