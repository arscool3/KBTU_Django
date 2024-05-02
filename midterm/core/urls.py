from django.urls import path
from rest_framework import routers

from core.views import *

# route = routers.SimpleRouter()
# route.register

# urlpatterns = route.urls

urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/student/', register_student_view, name='register_student'),
    path('register/instructor/', register_instructor_view, name='register_instructor'),
    path('instructor/course/assignment', instructor_assignment, name='create_assignment'),
    path('student/all/', get_all_students, name='all_students'),
    path('student/courses/', student_courses, name='student_courses'),
    path('instructor/all/', get_all_instructors, name='all_instuctors'),
    path('instructor/courses/', instructor_courses, name='instructor_courses'),
    path('user/', get_user, name='get_user'),
    path('', get_all_courses, name='all_courses')
]
