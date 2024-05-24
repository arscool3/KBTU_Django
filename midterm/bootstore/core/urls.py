from django.contrib import admin
from django.urls import path

from core.views import login_view, check_view, get_books, logout_view, register_view, add_books, update_author, update_user_info, place_order, list_authors, list_publishers, user_profile

urlpatterns = [
    path('register/', register_view, name='register'),  
    path('login/', login_view, name='login'), 
    path('add_books/', add_books, name='add_books'),
    path('update_author/<int:author_id>/', update_author, name='update_author'),
    path('update_user_info/',update_user_info, name='update_user_info'),
    path('place_order/', place_order, name='place_order'),
    
    path('check/', check_view, name='check'),
    path('books/', get_books, name='get_books'),
    path("logout/", logout_view, name='logout'),
    path('authors/', list_authors, name='list_authors'),
    path('publishers/',list_publishers, name='list_publishers'),
    path('profile/', user_profile, name='user_profile'),
]