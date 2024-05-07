from django.contrib import admin
from django.urls import path

from base.views import * 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('my_profile/', my_profile, name='my_profile'),

    path('profiles/<str:username>/', profile, name='profile'),
    path('profile_list',profile_list, name='profile_list'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('profiles/<str:username>/articles/', get_user_articles, name='user_articles'),
    path('profiles/<str:username>/followers/', get_user_followers, name='user_followers'),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path('check/', check_view, name='check'),
    
    path('add_topics/', add_topics, name='add_topics'),
    path('topics/', get_topics, name='topics'),
    path('hot_topic/',articles_by_hot_topic, name='hot_topic'),

    path('add_comments/<int:pk>/', add_comments, name='add_comments'),   
    path('add_likes/<int:pk>/', add_likes, name='add_likes'),
    path('add_follows/<str:username>/',add_follows,name='add_follows'),
    
    path('article_detail/<int:pk>/', article_detail, name='article_detail'),
    path('articles/<int:pk>/liked_users/', liked_users, name='liked_users'),
    path('articles/<int:pk>/article_comments/', article_comments, name='article_comments'),
    path('articles/', get_articles, name='articles'),
    path('add_articles/', add_articles, name='add_articles'),
    path('update_articles/<int:pk>/', update_articles, name='update_articles'),
    path('delete_articles/<int:pk>/', delete_articles, name='delete_articles'),

    path('articles/<int:pk>/add_to_reading_list/', add_to_reading_list, name='add_to_reading_list'),
    path('readinglists/',get_readinglists,name='readinglists'),



]