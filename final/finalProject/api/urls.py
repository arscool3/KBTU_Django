from django.urls import path, include
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, TourViewSet, ReviewViewSet, RequestViewSet, RatingViewSet, tour_list
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


router = DefaultRouter()
router.register(r'locations', LocationViewSet)
router.register(r'tours', TourViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'requests', RequestViewSet)
router.register(r'ratings', RatingViewSet)

urlpatterns = [
    path('tours/template', tour_list),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
