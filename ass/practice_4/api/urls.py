from django.contrib import admin
from django.urls import path
from .views import get_books, add_books, get_book

urlpatterns = [
    path('books/', get_books, name='books'),
    path('add_books/', add_books, name='add_books'),
    path('books/<int:pk>/', get_book, name='get_book'),
    ]