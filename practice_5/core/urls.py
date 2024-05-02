from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('author/add', create_author),
    path('post/add', create_post),
    path('storynote/add/', create_story_note),
    path('comment/add/', create_comment),
    path('post/all/', get_all_posts),
    path('post/select/', select_posts_by_author),
    path('post/comments/', select_comments_by_post),
    path('author/comments/', select_comments_by_author),
]