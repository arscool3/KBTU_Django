
from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.addComputer, name='addComputer'),
    path('computers', views.getComputers, name='getComputers')
]
