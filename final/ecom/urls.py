from django.urls import path
from .views import *

urlpatterns = [
    path("signup/", UserRegistrationAPIView.as_view(), name="registration"),
    path("signin/", UserLoginAPIView.as_view(), name="login"),
    path("products/", ProductViewSet.as_view({'post': 'create', 'get': 'list'}), name="products"),
    path("category/", CategoryViewSet.as_view({'post': 'create', 'get': 'list'}), name="category"),
    path("comments/", CommentViewSet.as_view({'post': 'create', 'get': 'list'}), name="comments"),
    path("likes/", LikeViewSet.as_view({'post': 'create', 'get': 'list'}), name="likes"),
]