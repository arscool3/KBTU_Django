from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('form/', lesson4view)
]