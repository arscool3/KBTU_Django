from django.urls import path
from . import views
from .views import user_login

urlpatterns = [
    path('', views.home, name='home'),
    path('vacancies/', views.vacancy_list, name='vacancy_list'),
    path('vacancy/<int:vacancy_id>/', views.vacancy_detail, name='vacancy_detail'),
    path('companies/', views.company_list, name='company_list'),
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),
    path('edit_profile/<int:user_id>/', views.edit_profile, name='edit_profile'),
    path('register/', views.register_user, name='register'),
    path('login/', user_login, name='login'),
    path('create_resume/', views.create_resume, name='create_resume'),
    path('apply_for_vacancy/<int:vacancy_id>/', views.apply_for_vacancy, name='apply_for_vacancy'),
    path('edit_resume/<int:resume_id>/', views.edit_resume, name='edit_resume'),
]
