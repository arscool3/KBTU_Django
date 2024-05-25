from django.contrib import admin
from django.urls import path

from .views import index, cat, divide

urlpatterns = [
    path("", index, name='index'),
    path("cat/", cat, name="cat"),
    path("divide/<int:number>", divide, name='test'),
]