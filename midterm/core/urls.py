from django.contrib import admin
from django.urls import path

from core.views import *
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('check/', check_view, name='check'),
    path('logout/', logout_view, name='logout'),
    path('gist/', gistReq, name='gist'),
    path('gist/<int:gist_id>', commitReq, name='commit'),
    path('commit/<int:commit_id>', fileReq, name='file')
]