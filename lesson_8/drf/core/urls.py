from django.urls import path
from rest_framework import routers

from core.views import WeatherViewSet

router = routers.SimpleRouter()
router.register(r"weather", WeatherViewSet)
urlpatterns = [] + router.urls