from django.contrib import admin
from django.urls import path

from core.views import login_view, check_view, get_articles
from core.views import logout_view, register_view, add_articles,add_likes,add_readinglists
from core.views import get_comments,add_comments,get_followers,get_likes,add_follows
from core.views import update_articles,delete_articles,add_topics,get_topics,get_readinglists

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('check/', check_view, name='check'),
    path('articles/', get_articles, name='articles'),
    path('readinglists/',get_readinglists,name='readinglists'),
    path('add_readinglists/',add_readinglists,name='add_readinglists'),
    path('comments/', get_comments, name='comments'),
    path("logout/", logout_view, name='logout'),
    path('add_articles/', add_articles, name='add_articles'),
    path('update_articles/<int:pk>/', update_articles, name='update_articles'),
    path('delete_articles/<int:pk>/', delete_articles, name='delete_articles'),
    path('add_topics/', add_topics, name='add_topics'),
    path('topics/', get_topics, name='get_topics'),
    path('add_comments/', add_comments, name='add_comments'),
    path('add_likes/<int:pk>/', add_likes, name='add_likes'),
    path('follows/',get_followers,name='follows'),
    path('add_follows/<str:username>/',add_follows,name='add_follows'),
    path('likes/',get_likes,name='likes'),
]