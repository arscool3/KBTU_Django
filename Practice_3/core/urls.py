from django.contrib import admin
from django.urls import path

from .views import user_create_view

urlpatterns = [
    path('create_user/', user_create_view, name='create_user_post'),
]