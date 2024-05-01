from django.contrib import admin
from django.urls import path

from views import *

urlpatterns = [
    path('students/', get_students),
    path('lessons/', get_lessons),
]