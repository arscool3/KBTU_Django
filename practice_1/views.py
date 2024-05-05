from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello Word!")

def home(request):
    return HttpResponse("Welcome to the homepage!")

def about(request):
    return HttpResponse("This is the about page.")
