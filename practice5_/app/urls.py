
from django.contrib import admin
from django.urls import path
from .views import corporations_and_departments
urlpatterns = [
    path('corporations/',corporations_and_departments, name='corporations')
]
