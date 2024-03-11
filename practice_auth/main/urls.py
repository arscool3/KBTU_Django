
from django.contrib import admin
from django.urls import path, include
from main.views import login_view, check_view, get_movies, logout_view, register_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('check/', check_view, name='check'),
    path('movies/', get_movies, name='movies'),
    path("logout/", logout_view, name='logout'),
]
