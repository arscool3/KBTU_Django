from django.shortcuts import render
from django.http import HttpResponse

breaking_bad = [
    "Walter White",
    "Mike Ehrmantraut",
    "Jesse Pinkman"
]

def index(request):
    return render(request, "index.html", {'bb':breaking_bad})

def exp(request, id):
    return HttpResponse(f"5^{id}={5**id}")

def welcome(request):
    return render(request, "index.html", {'bb':["welcome","willkommen","benvenuti"]})