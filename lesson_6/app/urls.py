from django.contrib import admin
from django.urls import path

from app.views import get_students, get_lessons

urlpatterns = [
    path('students/', get_students),
    path('lessons/', get_lessons),
]