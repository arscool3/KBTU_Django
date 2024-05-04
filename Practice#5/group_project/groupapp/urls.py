from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.create_book, name='create_book'),
    # ... other URL patterns for managing authors, reviewers, reviews, etc.
]
