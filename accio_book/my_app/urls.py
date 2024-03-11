from django.contrib import admin
from django.urls import path

from my_app.views import login_view, check_view, logout_view, register_view, homepage
from . import views

urlpatterns = [
    path('', homepage, name='homepage'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('check/', check_view, name='check'),
    path("logout/", logout_view, name='logout'),
    path('books/', views.get_all_books, name='get_all_books'),
    path('books/<int:book_id>/', views.get_book_details, name='get_book_details'),
    path('authors/', views.get_all_authors, name='get_all_authors'),
    path('authors/<int:author_id>/', views.get_author_details, name='get_author_details'),
    path('user/profile/', views.get_user_profile, name='get_user_profile'),
    path('user/favorite/', views.get_user_favorite, name='get_user_favorite'),
    path('add_book/', views.add_book, name='add_book'),
    path('add_authors/', views.add_author, name='add_author'),
    path('add_favorite/', views.add_favorite, name='add_favorite'),
    path('genres/add/', views.add_genre, name='add_genre'),
    path('user/profile/add/', views.add_user_profile, name='add_user_profile'),
    path('user/photo/add/', views.add_user_photo, name='add_user_photo'),
    
]