from django.contrib import admin
from django.urls import path

from .views import CourseListCreateAPIView, CourseDetailView, EnrollmentFormAPIView, CreateLessonAPIView, \
    TakeQuizAPIView

urlpatterns = [
    path('courses/', CourseListCreateAPIView.as_view(), name='list_courses'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('courses/<int:course_id>/enroll/', EnrollmentFormAPIView.as_view(), name='enrollment_form'),
    path('courses/<int:course_id>/lessons/create/', CreateLessonAPIView.as_view(), name='create_lesson'),
    path('quizzes/<int:pk>/', TakeQuizAPIView.as_view(), name='take_quiz'),
]