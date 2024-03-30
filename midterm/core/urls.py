from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

from core.views import CustomerViewSet

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"customers", CustomerViewSet)

urlpatterns = [] + router.urls


