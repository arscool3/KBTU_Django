from django.urls import path
from rest_framework import routers
from api.views import *

router = routers.SimpleRouter()
router.register(r'users',UserViewSet)
router.register(r'customers',CustomerViewSet)
router.register(r'manufacturers',ManufacturerViewSet)
router.register(r'categories',CategoryViewSet)
router.register(r'products',ProductViewSet)
router.register(r'history',HistoryItemViewSet)
router.register(r'comments',CommentViewSet)
urlpatterns = router.urls