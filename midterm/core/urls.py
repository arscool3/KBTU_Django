from django.contrib import admin
from django.urls import path

from core.views import *

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    #POST
    path('login/', login_view, name='login'),
    path('register/student/', register_student_view, name='register_student'),
    path('register/instructor/', register_instructor_view, name='register_instructor'),
    path('instructor/course/add/', instructor_create_course, name='add_course'),
    path('student/course/add', student_add_course, name='student_add_course'),
    path('instructor/course/assignment/create', instructor_create_assignment, name='create_assignment'),
    #GET
    path('course/all/', get_all_courses, name='all_courses'),
    path('student/all/', get_all_students, name='all_students'),
    path('student/courses/', get_student_courses, name='student_courses'),
    path('instructor/all/', get_all_instructors, name='all_instuctors'),
    path('instructor/courses/', get_instructor_courses, name='instructor_courses'),
    path('user/', get_user, name='get_user'),
]
