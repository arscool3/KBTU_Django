from django.urls import path, include
from .views import *
urlpatterns = [
    path('active-airplanes/', get_active_airplanes, name='active_airplanes'),
    path('inactive-airplanes/', get_inactive_airplanes, name='inactive_airplanes'),
    path('phone/<str:phone_number>/', get_by_phone_number, name='consumers_by_phone'),
    path('email/<str:email>/', get_by_email, name='consumers_by_email'),
    path('create-ticket/', create_ticket, name='create_ticket'),
    path('create-consumer/', create_consumer, name='create_consumer'),
    path('create-airplane/', create_airplane, name='create_airplane')
]