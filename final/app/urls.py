from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r"worker", WorkerViewSet)
router.register(r"customer", CustomerViewSet)
router.register(r"stock", StockViewSet)
router.register(r"product", ProductViewSet)
router.register(r"products_in_stock", ProductsInStockViewSet)
router.register(r"order", OrderViewSet)
router.register(r"delivery", DeliveryViewSet)

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('worker_create/', CreateWorkerView.as_view()),
    path('customer_create/', CreateCustomerView.as_view())
]
