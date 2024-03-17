from django.contrib import admin
from django.urls import path

from .views import list_of_students

urlpatterns = [
    path("students/", list_of_students, name='students')
]