from django.urls import path

from coursera.views import *

urlpatterns = [
    path('courses/', get_courses,name='courses'),
    path('create-course', create_course, name='create-course'),
    path('courses/<int:course_id>/', get_course_details, name='course_details'),
    path('enrollments/', get_enrollments, name='enrollments'),
    path('create-enrollment', create_enrollment, name='create-enrollment'),
    path('enrollments/<int:course_id>/', get_course_enrollments, name='get_course_enrollments'),
    path('instructors/', get_instructors, name='instructors'),
    path('create-instructor', create_instructor, name='create-instructor'),
    path('review/', get_reviews, name='reviews'),
    path('create-review', create_review, name='create-review'),
    path('lesson/', get_lessons, name='lessons'),
    path('create-lesson', create_lesson, name='create-lesson'),
    path('register/', register_student, name='register'),
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name='logout'),
]
