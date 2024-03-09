from django.urls import path
from app.views import *

urlpatterns = [
    path('register', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('', about_view, name='about'),
    path('logout/', logout_view, name='logout'),
    path('schedule/', schedule_view, name='schedule'),
    path('disciplines/', disciplines_view, name='disciplines'),
    path('journal/', journal_view, name='journal'),
    path('news/', news_view, name='news'),
    path('profile/', profile_view, name='profile'),
    # path('add_schedule/', add_schedule, name='add_schedule'),
    # path('edit_schedule/', edit_schedule, name='edit_schedule'),
    # path('delete_schedule/', delete_schedule, name='delete_schedule'),
    # path('schedule_list/', schedule_list, name='schedule_list'),
]
