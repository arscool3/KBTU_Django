from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('fitness_user/', fitness_user_view, name='fitness_user'),
    path('activity/', activity_view, name='activity'),
    path('diet/', diet_view, name='diet'),
    path('health_metrics/', health_metrics_view, name='health_metrics'),
    path('goal/', goal_view, name='goal'),
    path('progress/', progress_view, name='progress'),
    path('check_fitness_user/', check_fitness_user, name='check_fitness_user'),
    path('check_activities/', check_activities, name='check_activities'),
    path('check_diets/', check_diets, name='check_diets'),
    path('check_health_metrics/', check_health_metrics, name='check_health_metrics'),
    path('check_goal/', check_goal, name='check_goal'),
    path('check_progress/', check_progress, name='check_progress'),
]
