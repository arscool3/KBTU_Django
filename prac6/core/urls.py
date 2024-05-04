# urls.py (project-level)
from django.urls import path, include
from rest_framework import routers
from .views import AnimalViewSet

router = routers.DefaultRouter()
router.register(r'animals', AnimalViewSet)

urlpatterns = [
    # Other URL patterns
    path('api/', include(router.urls)),
]
