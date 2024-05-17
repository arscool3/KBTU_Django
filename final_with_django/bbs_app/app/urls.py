from django.urls import path, include
from rest_framework import routers
from .views import ManagerViewSet, BarberViewSet, ClientViewSet, BarbershopViewSet, BookingRequestViewSet, ApplicationRequestViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'managers', ManagerViewSet)
router.register(r'barbers', BarberViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'barbershops', BarbershopViewSet)
router.register(r'booking-requests', BookingRequestViewSet)
router.register(r'application-requests', ApplicationRequestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
