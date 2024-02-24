from django.shortcuts import render
from django.http import HttpResponse

def main_view(request):
    return HttpResponse ("this is probably main view")

def basic_view(request):
    return HttpResponse("this might be basic view")

def test_view(request):
    return HttpResponse("this is most definetily test view")