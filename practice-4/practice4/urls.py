# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.list_published_posts, name='list_posts'),
    path('categories/', views.list_active_categories, name='list_categories'),
    path('posts/create/', views.create_post, name='create_post'),
]
