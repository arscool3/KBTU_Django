from django.urls import path
from .views import posts_list, comments_list

urlpatterns = [
    path('posts/', posts_list, name='posts_list'),
    path('comments/', comments_list, name='comments_list'),
]
