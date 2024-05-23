from django.urls import path
from app.views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'faculties-modelviews', FacultyModelViewSet)
router.register(r'specialities-modelviews', SpecialityModelViewSet)
router.register(r'disciplines-modelviews', DisciplineModelViewSet)
router.register(r'students-modelviews', StudentModelViewSet)
router.register(r'professors-modelviews', ProfessorModelViewSet)
router.register(r'schedules-modelviews', ScheduleModelViewSet)
router.register(r'news-modelviews', NewsModelViewSet)

urlpatterns = [

    # get endpoints
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('', about_view, name='about'),
    path('basic/', basic_view, name='basic'),
    path('logout/', logout_view, name='logout'),
    path('schedule/', schedule_view, name='schedule'),
    path('disciplines/', disciplines_view, name='disciplines'),
    path('journal/', journal_view, name='journal'),
    path('news/', news_view, name='news'),
    path('profile/', profile_view, name='profile'),
    path('settings/', settings_view, name='settings'),


    # post endpoints 
    path('crud_news/', crud_news, name='crud_news'),
    path('crud_student/', crud_student, name='crud_student'),
    path('crud_faculty/', crud_faculty, name='crud_faculty'),
    path('crud_schedule/', crud_schedule, name='crud_schedule'),
    path('crud_professor/', crud_professor, name='crud_professor'),
    path('crud_discipline/', crud_discipline, name='crud_discipline'),
    path('crud_speciality/', crud_speciality, name='crud_speciality'),

]

urlpatterns += router.urls