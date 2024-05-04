from django.contrib import admin
from django.urls import path

from myapp.views import view

urlpatterns = [
    path('', view),
]