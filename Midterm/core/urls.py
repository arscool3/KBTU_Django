from django.urls import path
from core.views import login_view, check_view

from core.views import get_country_by_name, get_cities, get_citizens, get_cars, get_only_german_cars, get_only_usa_cars, get_only_new_cars, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('check/', check_view, name='check'),
    path('logout/', logout_view, name='logout'),
    path('countries/', get_country_by_name),
    path('cities/', get_cities),
    path('citizens/', get_citizens),
    path('cars/', get_cars),
    path('newcars/', get_only_new_cars),
    path('germancars/', get_only_german_cars),
    path('usacars/', get_only_usa_cars),
]
