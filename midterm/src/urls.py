"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

import Project.views

router = DefaultRouter()
router.register(r'projects', Project.views.ProjectViewSet, basename='project')
router.register(r'users', Project.views.UserViewSet, basename='user')
router.register(r'tasks', Project.views.TaskViewSet, basename='user')
router.register(r'comments', Project.views.CommentViewSet, basename='user')
router.register(r'attachments', Project.views.AttachmentViewSet, basename='user')
router.register(r'teams', Project.views.TeamViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Project.views.login_view, name='login'),
    path('register/', Project.views.register_view, name='register'),
    path('project/dates', Project.views.get_projects_by_date, name='dates'),
    path('project/status', Project.views.get_only_build_company, name='status'),
    path('project/dates/january', Project.views.get_projects_from_january, name='status'),
    path('', include(router.urls))
]
