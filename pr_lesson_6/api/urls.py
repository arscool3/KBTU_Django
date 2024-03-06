from django.urls import path

from .views import *

urlpatterns = [
    path('users/', get_users),
    # path('users/<int:pk>/', get_user),
    path('user/', get_user)
]