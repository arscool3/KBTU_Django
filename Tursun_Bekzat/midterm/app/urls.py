from django.urls import path
from app.views import *

urlpatterns = [
    path('register', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('schedule/', schedule_view, name='schedule'),
    path('disciplines/', disciplines_view, name='disciplines'),
    path('journal/', journal_view, name='journal'),
    path('news/', news_view, name='news'),
    path('profile/', profile_view, name='profile'),
]
