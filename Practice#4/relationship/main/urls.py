from django.urls import path
from . import views

urlpatterns = [
    path('managers/', views.manager_list, name='manager_list'),
    path('departments/', views.department_list, name='department_list'),
    path('employees/', views.employee_list, name='employee_list'),
    path('projects/', views.project_list, name='project_list'),
]
