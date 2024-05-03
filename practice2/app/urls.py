from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name='index'),
    path("students/", get_students, name='students')
]