from django.urls import path

from library.views import *

urlpatterns = [
    path('genres/', genre_list, name='genres-list'),
    path('genres/<int:pk>/', genre_detail, name='genre-detail'),
    path('genres/create', add_genre, name='add_genre'),
    path('books/', book_list, name='books-list'),
    path('authors/', author_list, name='authors-list'),
    path('borrower/', borrower_list, name='borrower-list'),
    path('authors/<int:pk>/', author_detail, name='author-detail'),
    path('borrower/<int:pk>/', borrower_detail, name='borrower-detail'),
    path('books/<int:pk>/', book_detail, name='book-detail'),
    path('books/create', add_book, name='add_book'),

]