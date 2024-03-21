from django.http import HttpResponse
from django.shortcuts import render


students = [
    'Askar',
    'Aliya',
    'Alen',
]

teachers = [
    'Arslan',
    'Yelibay',
    'Bobur',
]

def view(request):
    return render(request, 'main.html', {'students': students, 'teachers': teachers})
