from django.contrib import admin
from django.urls import path

from myapp.views import login_view, check_view, get_movies, logout_view, register_view, add_movies, delete_movie

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('check/', check_view, name='check'),
    path('movies/', get_movies, name='movies'),
    path("logout/", logout_view, name='logout'),
    path('add_movies/', add_movies, name='add_movies'),
    path('movies/<int:movie_id>/delete/', delete_movie, name='delete_movie'),
]