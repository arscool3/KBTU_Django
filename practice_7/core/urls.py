from django.urls import path
from rest_framework import routers
from core.views import CosmeticProductViewSet

router = routers.SimpleRouter()
router.register(r"cosmetic-products", CosmeticProductViewSet)
urlpatterns = [] + router.urls
