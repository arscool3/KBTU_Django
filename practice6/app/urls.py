from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/vacancies/', views.VacancyListCreateAPIView.as_view(), name='vacancy-list'),
    path('api/vacancies/<int:pk>/', views.VacancyRetrieveUpdateDestroyAPIView.as_view(), name='vacancy-detail'),
    path('api/companies/', views.CompanyListAPIView.as_view(), name='company-list'),
    path('api/companies/<int:pk>/', views.CompanyDetailAPIView.as_view(), name='company-detail'),
    path('api/user/', views.UserRetrieveUpdateAPIView.as_view(), name='user-profile'),
    path('api/user/change-password/', views.ChangePasswordAPIView.as_view(), name='change-password'),
    path('api/resumes/', views.ResumeListCreateAPIView.as_view(), name='resume-list'),
    path('api/resumes/<int:pk>/', views.ResumeRetrieveUpdateDestroyAPIView.as_view(), name='resume-detail'),
    path('api/user/register/', views.UserCreateAPIView.as_view(), name='user-register'),
    path('api/user/login/', views.user_login, name='user-login'),
    path('api/resumes/create/', views.create_resume, name='create-resume'),
    path('api/vacancies/<int:vacancy_id>/apply/', views.apply_for_vacancy, name='apply-for-vacancy'),
]