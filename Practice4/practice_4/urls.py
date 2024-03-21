from django.urls import path
from .views import get_books_by_author, get_publishers_with_magazines, create_book, get_authors

urlpatterns = [
    path('books-by-author/<str:author_name>/', get_books_by_author, name='books_by_author'),
    path('publishers-with-magazines/', get_publishers_with_magazines, name='publishers_with_magazines'),
    path('create-book/', create_book, name='create_book'),
    path('authors-with-books/', get_authors, name='authors_with_books'),  # Added new URL for get_authors
]
