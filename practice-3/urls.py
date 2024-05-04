from django.urls import path

from practice3.views import *

urlpatterns = [
    # Practice - 3
    path("", user_create, name='user_create'),
    path("success_url", success, name='success_url'),
]