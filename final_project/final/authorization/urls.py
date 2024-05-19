from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'auth', UserViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
]
