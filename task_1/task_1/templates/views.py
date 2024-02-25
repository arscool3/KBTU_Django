from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("This is main view")

def index_1(request):
    return HttpResponse("This is basic view")

def index_2(request):
    return HttpResponse("Test view")
