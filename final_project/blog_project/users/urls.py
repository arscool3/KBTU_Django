from django.urls import include, path

from users.viewsets import CustomUserViewSet
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),

    # Viewsets
    path('', include(router.urls)),
]
