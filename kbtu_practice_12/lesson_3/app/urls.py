from django.contrib import admin
from django.urls import path

from app.views import view

urlpatterns = [
    path('app/', view)
]
