from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', addposts, name='addPost')
]