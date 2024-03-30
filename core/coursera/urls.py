from django.urls import path
from rest_framework import routers

from coursera.views import *


urlpatterns = [
    path('courses/', get_courses, name='courses'),
    path('courses/drf', CourseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('create-course', create_course, name='create-course'),
    path('register/', register_student, name='register'),
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name='logout'),
]
