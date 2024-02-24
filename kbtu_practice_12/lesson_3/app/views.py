from django.http import HttpResponse
from django.shortcuts import render

students = ['aliya', 'Askar', 'leyla']
teachers = ['arslan']


def view(request):
    return render(request, 'main.html', {'students': students, 'teachers': teachers})

