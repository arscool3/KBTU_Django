from django.contrib import admin
from django.urls import path

from core.views import * 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path('check/', check_view, name='check'),
    
    path('add_topics/', add_topics, name='add_topics'),
    path('topics/', get_topics, name='get_topics'),

    path('articles/', get_articles, name='articles'),
    path('add_articles/', add_articles, name='add_articles'),
    path('update_articles/<int:pk>/', update_articles, name='update_articles'),
    path('delete_articles/<int:pk>/', delete_articles, name='delete_articles'),

    path('add_readinglists/',add_readinglists,name='add_readinglists'),
    path('readinglists/',get_readinglists,name='readinglists'),

    path('comments/', get_comments, name='comments'),
    path('add_comments/', add_comments, name='add_comments'),
    
    path('add_likes/<int:pk>/', add_likes, name='add_likes'),
    path('likes/',get_likes,name='likes'),
    path('add_follows/<str:username>/',add_follows,name='add_follows'),

]