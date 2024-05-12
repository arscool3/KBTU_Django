from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet, CompanyViewSet, SkillViewSet, VacancyViewSet, ResumeViewSet, ResponseViewSet
from .views import vacancy_list, company_list, register_user, user_login

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'companies', CompanyViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'vacancies', VacancyViewSet)
router.register(r'resumes', ResumeViewSet)
router.register(r'responses', ResponseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('vacancy_list/', vacancy_list, name='vacancy_list'),
    path('company_list/', company_list, name='company_list'),
    path('register/', register_user, name='register'),
    path('login/', user_login, name='login'),
]
