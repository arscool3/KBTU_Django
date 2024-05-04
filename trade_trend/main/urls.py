from django.contrib import admin
from django.urls import path, include
from main.views import get_index
urlpatterns = [
    path('', get_index)
]