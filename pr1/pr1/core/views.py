from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def main(request):
    return HttpResponse("Hello, main!")

def test(request):
    return HttpResponse("Hello, test!")