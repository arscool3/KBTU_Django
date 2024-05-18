from django.urls import path, include
from rest_framework import routers
from .views import (ManagerViewSet, 
                    BarberViewSet, 
                    ClientViewSet, 
                    BarbershopViewSet, 
                    BookingRequestViewSet, 
                    ApplicationRequestViewSet, 
                    UserViewSet, barbers_list, 
                    barbershops_list, homepage, login_view, register, logout_view, managers_list, user_detail, users_list)

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
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('home/', homepage, name='homepage'),
    path('managers_list/', managers_list, name='managers_list'),
    path('barbers_list/', barbers_list, name='barbers_list'),
    path('barbershops_list/', barbershops_list, name='barbershops_list'),
    path('users_list/', users_list, name='users_list'),
    path('users_list/<int:user_id>/', user_detail, name='user_detail'),
]
