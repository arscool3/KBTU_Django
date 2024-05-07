from django.urls import path
from . import views

urlpatterns = [
    path('student/add/', views.add_student, name='add_student'),
    path('student/<int:student_id>/', views.get_student, name='get_student'),
    path('course/add/', views.add_course, name='add_course'),
    path('course/<int:course_id>/', views.get_course, name='get_course'),
    path('teacher/add/', views.add_teacher, name='add_teacher'),
    path('teacher/<int:teacher_id>/', views.get_teacher, name='get_teacher'),
    path('courses/', views.list_courses, name='list_courses'),
    path('enroll/', views.enroll_student, name='enroll_student')
]
