from django.urls import path
from core.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('my_profile/', ProfileDetailView.as_view(), name='my_profile'),

    path('profiles/<str:username>/', ProfileDetailView.as_view(), name='profile'),
    path('profile_list/', ProfileListView.as_view(), name='profile_list'),
    path('edit_profile/', ProfileUpdateView.as_view(), name='edit_profile'),
    path('profiles/<str:username>/articles/', ArticleListView.as_view(), name='user_articles'),
    path('profiles/<str:username>/followers/', get_user_followers, name='user_followers'),

    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name='logout'),
    path('check/', check_view, name='check'),
    
    path('add_topics/', TopicCreateView.as_view(), name='add_topics'),
    path('topics/', TopicListView.as_view(), name='topics'),
    path('hot_topic/', articles_by_hot_topic, name='hot_topic'),

    path('add_comments/<int:pk>/', CommentCreateView.as_view(), name='add_comments'),   
    path('add_likes/<int:pk>/', LikeCreateView.as_view(), name='add_likes'),
    path('add_follows/<str:username>/', FollowCreateView.as_view(), name='add_follows'),
    
    path('article_detail/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<int:pk>/liked_users/', liked_users, name='liked_users'),
    path('articles/<int:pk>/article_comments/', article_comments, name='article_comments'),
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('add_articles/', ArticleCreateView.as_view(), name='add_articles'),
    path('update_articles/<int:pk>/', ArticleUpdateView.as_view(), name='update_articles'),
    path('delete_articles/<int:pk>/', ArticleDeleteView.as_view(), name='delete_articles'),

    path('articles/<int:pk>/add_to_reading_list/', ReadingListCreateView.as_view(), name='add_to_reading_list'),
    path('readinglists/', ReadingListView.as_view(), name='readinglists'),
]
