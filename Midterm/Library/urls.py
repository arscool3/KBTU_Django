from django.urls import path

from Library.views import *

urlpatterns = [
    path('add_book/', add_book, name='add_book'),
    path('add_author/', add_author, name='add_author'),
    path('add_genre/', add_genre, name='add_genre'),
    path('add_client/', add_client, name='add_client'),
    path('add_loan/', add_loan, name='add_loan'),
    path('add_publishing_office/', add_publishing_office, name='add_publishing_office'),

    path('books/', get_books, name='get_books'),
    path('books/<int:book_id>/', get_book_by_id, name='get_book_by_id'),
    path('genres/', get_genres, name='get_genres'),
    path('authors/', get_authors, name='get_authors'),
    path('clients/', get_clients, name='get_clients'),
    path('loans/', get_loans, name='get_loans'),
    path('publishing_office/', get_publishing_office, name='get_publishing_office'),
    path('delete_loan/<int:book_id>/<int:client_id>/', delete_loan, name='delete_loan'),
    path('books_by_genre/<int:genre__id>/', get_books_by_genre, name='books_by_genre'),
]