from django.urls import path
from .views import *

urlpatterns = [
    path('readers/', get_readers, name='get_readers'),
    path('authors/<int:author_id>/books/', get_books_by_author, name='get_books_by_author'),
    path('genres/<int:genre_id>/books/', get_books_by_genre, name='get_books_by_genre'),
    path('books/', get_books, name='get_books'),
    path('authors/', get_authors, name='get_authors'),
    path('genres/',get_genres, name='get_genres'),
    path('books/create/', create_book, name='create_book'),
    path('authors/create/', create_author, name='create_author'),
    path('genres/create/', create_genre, name='create_genre'),
]