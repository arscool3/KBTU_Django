from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets

from .serializers import GroupSerializer, UserSerializer
from django.http import HttpResponse
from django.shortcuts import render


from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def main(request):
    return HttpResponse("This is main page")

def more(request):
    return HttpResponse("This is more page")

def test(request):
    return HttpResponse("This is test page")