from django.contrib import admin
from django.urls import path
from .views import corporations_and_departments, get_employees_age, get_employees_salary, get_projects

urlpatterns = [
    path('corporations/',corporations_and_departments, name='corporations'),
    path('employees/age/', get_employees_age),
    path('employees/salary/', get_employees_salary),
    path('projects/', get_projects),
]
