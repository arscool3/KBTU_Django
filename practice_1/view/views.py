from django.shortcuts import render
from django.http import HttpResponse

def main_view(request):
    return HttpResponse("This is the Main View")

def basic_view(request):
    return HttpResponse("This is the Basic View")

def test_view(request):
    return HttpResponse("This is the Test View")

