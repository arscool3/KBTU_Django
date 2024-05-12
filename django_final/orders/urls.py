from rest_framework.routers import DefaultRouter

from orders.views import OrderViewSet

router = DefaultRouter()

router.register(r"order", OrderViewSet)

urlpatterns = router.urls
