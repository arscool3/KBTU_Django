from django.contrib import admin
from django.urls import path
from .views import view, success_view

urlpatterns = [
    path('', view, name='view'),
    path('success/', success_view, name='success'),
]