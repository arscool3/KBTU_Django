from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def main_view(request):
    return HttpResponse("This is main view")

def basic_view(request):
    return HttpResponse("This is basic view")

def test_view(request):
    return HttpResponse("Test View")