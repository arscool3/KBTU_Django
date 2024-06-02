from django.urls import path,include
from .views import *
from rest_framework import routers

#router = routers.SimpleRouter()
#router.register(r"courses", CourseViewSet.as_view({'get':'list'}), basename="Course")

urlpatterns = [
    path('', index, name='index'),
    path('auth/signin/',signin,name='signin'),
    path('auth/signup/',signup,name='signup'),
    path('auth/signout/',signout,name='signout'),
    path('profile/',profile,name='profile'),
    #path('', include(router.urls)),
    path('courses/',CourseViewSet.as_view({'get':'list'}),name="courses"),
    #path('courses/',courses,name='courses'),
    #path('courses/<int:id>',course,name='course'),
    #path('courses/new',newcourse,name='newcourse'),
    path('lessons/<int:id>',lesson,name='lesson'),
    path('lessons/new',newlesson,name='newlesson'),
    path('quiz/<int:id>/answer',answer,name='answer'),
    path('quiz/<int:id>/new',newquestion,name='newquestion'),
    path('orgs/<int:id>',org,name='orgs'),
    path('orgs/new',neworg,name='neworg'),
]