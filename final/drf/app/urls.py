from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, EmployeeViewSet, ProjectViewSet, TaskViewSet, ReportViewSet, SalaryViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'reports', ReportViewSet)
router.register(r'salaries', SalaryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]