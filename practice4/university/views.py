from django.shortcuts import render
from django.http import HttpResponse

from .models import University, Faculty, Speciality, Student


def get_universities(request):
    universities = University.objects.all()
    return render(request, "home.html", {"items": universities, "object": "University"})


def get_faculties(request):
    faculties = Faculty.objects.all()
    return render(request, "home.html", {"items": faculties, "object": "Faculties"})


def get_specialities(request):
    specialities = Speciality.objects.all()
    return render(request, "home.html", {"items": specialities, "object": "Specialities"})


def get_students(request):
    students = Student.objects.all()
    return render(request, "home.html", {"items": students, "object": "Students"})