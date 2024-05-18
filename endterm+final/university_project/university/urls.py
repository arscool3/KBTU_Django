from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path, include

app_name = "university"

router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'courses', views.CourseViewSet)
router.register(r'students', views.StudentViewSet)
router.register(r'professors', views.ProfessorViewSet)
router.register(r'schedules', views.ScheduleViewSet)
router.register(r'grades', views.GradeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('update_course/<int:course_id>/', views.update_course, name='update_course'),
    # path('api/register/', views.RegisterView.as_view(), name='register'),

]
