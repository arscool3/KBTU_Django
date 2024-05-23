from django.contrib import admin
from django.urls import path

from students import views

urlpatterns = [
    path('list/', views.index),
    path('<int:id>/', views.stuName)
]