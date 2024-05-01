from django.urls import path

from .views import *

urlpatterns = [
    path('books', index, name='index'),
    path('users', get_users, name='get_users'),
    path('user/<int:user_id>', get_user, name='get_user'),
    path('add_book', add_book, name='add_book'),
    path('add_author', add_author, name='add_author'),
    path('add_publisher', add_publisher, name='add_publisher'),
    path('add_genre', add_genre, name='add_genre'),
    path('add_customer', add_customer, name='add_customer'),
    path('add_instance', add_instance, name='add_instance'),
]