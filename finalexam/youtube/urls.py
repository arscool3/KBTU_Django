from django.urls import path
from .views import (
    RegistrationAPIView,
    LoginAPIView,
    UserProfileView,
    PostViewSet,
    CommentViewSet,
    LikeViewSet,
    FollowViewSet
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'likes', LikeViewSet, basename='like')
router.register(r'follows', FollowViewSet, basename='follow')

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
]

urlpatterns += router.urls
