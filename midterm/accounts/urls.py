from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('paper-shelf/', paper_shelf, name='paper_shelf'),

]

