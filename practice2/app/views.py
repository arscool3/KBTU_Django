from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


students = ['Arslan', 'Beks']


def index(request):
    return HttpResponse("Hello World!")


def get_students(request):
    return render(request, 'index.html', {'students': students})