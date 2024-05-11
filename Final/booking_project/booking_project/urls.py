from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from booking_app.viewsets import BookingViewSet, ReviewViewSet, PaymentViewSet, NotificationViewSet
from booking_app.views import *
router = DefaultRouter()
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'notifications', NotificationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/bookings/user/', BookingByUserView.as_view(), name='booking_by_user'),
    path('api/bookings/theme/', BookingByThemeView.as_view(), name='booking_by_theme'),
]