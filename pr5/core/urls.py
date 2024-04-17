from django.urls import path
from views import *

urlpatterns = [
    path('add_book', add_book, name='add_book'),
    path('add_author', add_author, name='add_author'),
    path('add_member', add_member, name='add_member'),
    path('users', get_users, name='users'),
    path('user/<int:user_id>/borrow', borrow_book, name='borrow_book'),
    path('user/<int:author_id>', get_author, name='get_author'),
    path('books', get_books, name='get_books'),
    path('book/<int:book_id>', get_book, name='get_book')
]