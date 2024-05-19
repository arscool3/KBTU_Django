from django.contrib import admin
from django.urls import path
from .views import (
    LocationAPIDetailView,
    LocationAPIView,
    TourAPIView,
    TourAPIDetailView,
    ReviewAPIView,
    ReviewAPIDetailView,
    ReviewCreateAPIView,
    RequestAPICreate,
    RegistrationAPICreate
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('locations/', LocationAPIView.as_view()),
    path('locations/<int:pk>/', LocationAPIDetailView.as_view()),
    path('locations/<int:location_id>/tours/', TourAPIView.as_view()),
    path('locations/<int:location_id>/tours/<int:pk>', TourAPIDetailView.as_view()),

    path('reviews/', ReviewAPIView.as_view()),
    path('reviews/create/', ReviewCreateAPIView.as_view()),
    path('reviews/<int:pk>/', ReviewAPIDetailView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('request/', RequestAPICreate.as_view()),
    path('registration/', RegistrationAPICreate.as_view())


]