
from django.contrib import admin
from django.urls import path
from .views import get_bookstore

urlpatterns = [

    path('books/', get_bookstore, name='books')
]
