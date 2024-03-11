from django.urls import path
from .views import *

urlpatterns = [
    #auth
    path('register/', register, name='register'),
    path('login/', logIn, name='login'),
    path('profile/', profile, name='profile')
]