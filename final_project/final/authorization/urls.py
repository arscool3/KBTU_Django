from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename='auth')

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', include('rest_framework.urls')),
]
