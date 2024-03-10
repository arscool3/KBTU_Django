from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vacancies/', views.vacancy_list, name='vacancy_list'),
    path('vacancies/<int:vacancy_id>/', views.vacancy_detail, name='vacancy_detail'),
    path('companies/', views.company_list, name='company_list'),
    path('user/profile/', views.user_profile, name='user_profile'),
    path('user/edit-profile/', views.edit_profile, name='edit_profile'),
    path('register/', views.register_user, name='register_user'),
    path('login/', views.user_login, name='user_login'),
    path('create-resume/', views.create_resume, name='create_resume'),
    path('apply-to-vacancy/<int:vacancy_id>/', views.apply_to_vacancy, name='apply_to_vacancy'),
    path('save-vacancy/<int:vacancy_id>/', views.save_vacancy, name='save_vacancy'),
    path('edit-resume/', views.edit_resume, name='edit_resume'),
]