from django.contrib import admin
from django.urls import path

from .views import index, test, students_list

urlpatterns = [
    path('', index, name='index'),
    path('test/<int:id>', test, name='test'),
    path('', students_list, name='student_list'),
]
