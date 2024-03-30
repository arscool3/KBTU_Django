from django.urls import path
from coursera.views import *

urlpatterns = [
    path('courses/', get_courses,name='courses'),
    path('courses/drf', CourseViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('course/create', create_course, name='create-course'),
    path('courses/<int:course_id>/', get_course_details, name='course_details'),
    path('enrollments/', get_enrollments, name='enrollments'),
    path('enrollment/create', create_enrollment, name='create-enrollment'),
    path('enrollments/<int:course_id>/', get_course_enrollments, name='get_course_enrollments'),
    path('instructors/', get_instructors, name='instructors'),
    path('instructor/create', create_instructor, name='create-instructor'),
    path('review/', get_reviews, name='reviews'),
    path('review/create', create_review, name='create-review'),
    path('lesson/', get_lessons, name='lessons'),
    path('lesson/create', create_lesson, name='create-lesson'),
    path('register/', register_student, name='register'),
    path('login/', login_view, name='login'),
    path("logout/", logout_view, name='logout'),
]
