from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def main_view(request):
    s = "This is  main view"
    return HttpResponse(s)


def basic_view(request):
    s = "This is basic view"
    return HttpResponse(s)


def test_view(request):
    s = "Test View"
    return HttpResponse(s)
