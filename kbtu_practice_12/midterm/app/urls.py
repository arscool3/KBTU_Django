from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('auth/sign_in/', LoginView.as_view(template_name="login.html"), name="login-user"), 
    path('create_education/', create_education, name='create_education'),
    path('create_country/', create_country, name='create_country'),
    path('create_city/', create_city, name='create_city'),
    path('create_foreign_language/', create_foreign_language, name='create_foreign_language'),
    path('create_resume_employment_type/', create_resume_employment_type, name='create_resume_employment_type'),
    path('create_working_history/', create_working_history, name='create_working_history'),
    path('create_resume/', create_resume, name='create_resume'),
    path('create_employment_type/', create_employment_type, name='create_employment_type'),
    path('resumes/', get_resumes, name='resume_list'),
    path('resumes/<int:resume_id>/', get_resume_by_id, name='get_resume_by_id'),
    path('countries/', get_all_countries, name='get_all_countries'),
    path('countries/<int:country_id>/', get_country_by_id, name='get_country_by_id'),
    path('working_histories/', get_all_working_histories, name='get_all_working_histories'),
    path('working_histories/<int:working_history_id>/', get_working_history_by_id, name='get_working_history_by_id'),
]