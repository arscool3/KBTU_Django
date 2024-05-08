from django.contrib import admin
from django.urls import path
from manager_app.views import *

urlpatterns = [
    path('topics/add', add_topic),
    path('posts/add', add_post),
    path('comments/add', add_comment),
    path('author/add', add_author),
    path('posts/all', get_all_posts),
    path('topics/all', get_all_topics),
]