from django.urls import path, include
from core.views import check_view
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, CityViewSet, CitizenViewSet, CarViewSet
from core.views import get_country_by_name, get_cities, get_citizens, get_cars, get_only_german_cars, get_only_usa_cars, get_only_new_cars, logout_view


router = DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'cities', CityViewSet)
router.register(r'citizens', CitizenViewSet)
router.register(r'cars', CarViewSet)


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm),
         name='login'),
    path('check/', check_view, name='check'),
    path('logout/', logout_view, name='logout'),
    path('countries/', get_country_by_name),
    path('cities/', get_cities),
    path('citizens/', get_citizens),
    path('cars/', get_cars),
    path('newcars/', get_only_new_cars),
    path('germancars/', get_only_german_cars),
    path('usacars/', get_only_usa_cars),
    path('', include(router.urls)),
]
