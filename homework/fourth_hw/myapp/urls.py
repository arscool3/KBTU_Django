from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.authors, name='authors'),
    path('books/', views.books, name='books'),
    path('book/create/', views.book_create, name='book_create'),
]
