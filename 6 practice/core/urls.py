from django.contrib import admin
from django.urls import path

from core.views import *

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    #POST
    path('login/', login_view, name='login'),
    path('signup/', sign_up_choice, name='sign_up'),
    path('signup/student/', register_student_view, name='sign_up_student'),
    path('signup/instructor/', register_instructor_view, name='sign_up_instructor'),
    path('student/courses/', student_courses, name='student_courses'),
    path('instructor/course/assignment/create', instructor_create_assignment, name='create_assignment'),
    #GET
    path('course/all/', get_all_courses, name='all_courses'),
    path('student/all/', get_all_students, name='all_students'),
    path('instructor/courses/', instructor_courses, name='instructor_courses'),
    path('instructor/all/', get_all_instructors, name='all_instuctors'),    
    path('user/', get_user, name='get_user'),
    path('', get_all_courses, name='all_courses')
]
