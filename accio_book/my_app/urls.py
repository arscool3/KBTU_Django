from django.contrib import admin
from django.urls import path

from my_app.views import login_view, check_view, get_books, logout_view, register_view, add_books, homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('check/', check_view, name='check'),
    path('books/', get_books, name='books'),
    path("logout/", logout_view, name='logout'),
    path('add_books/', add_books, name='add_books'),
    
]