from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views
from .views import DriverLicenseViewSet, CarViewSet, ParkingLotViewSet, ParkingSpaceViewSet, PaymentViewSet, \
    parking_lot_detail, reserve_parking_space, user_profile, reserve, reservation_view

router = routers.DefaultRouter()
router.register(r'driverlicenses', DriverLicenseViewSet)
router.register(r'cars', CarViewSet)
router.register(r'parkinglots', ParkingLotViewSet)
router.register(r'parkingspaces', ParkingSpaceViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('parking_lot/<int:parking_lot_id>/', parking_lot_detail, name='parking_lot_detail'),
    path('parking_lot/<int:parking_lot_id>/parking_space/<int:space_id>/', reserve_parking_space,name='reserve_parking_space'),
    path('profile/', user_profile, name='user_profile'),
    path('api-auth/', include('rest_framework.urls')),
    path('process_payment/', views.process_parking_payment, name='process_payment'),
    path('reserve/', reservation_view, name='reservation'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
