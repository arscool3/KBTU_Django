from django.urls import path

from rest_framework import routers
from .views import CategoryViewSet, VoucherViewSet, UserViewSet, CommentViewSet, FavoriteViewSet, OrderViewSet


from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView,
)
from .views import categories_list, CommentsListAPIView, CommentDetailAPIView, categories_vouchers, vouchers_list, \
    vouchers_detail, get_favorites_by_user, favorite_list,get_favorite_by_voucher,home, \
    UsersListAPIView, UsersDetailAPIView, RegisterView, LoginView, LogoutView

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'vouchers', VoucherViewSet)
router.register(r'users', UserViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = [
    path('', home, name='home'),
    path('categories/<int:category_id>/', categories_vouchers, name='category_detail'),
    path('vouchers/<int:voucher_id>/', vouchers_detail, name='vouchers_detail'),
    path('vouchers/<int:voucher_id>/comments/', CommentsListAPIView.as_view(), name='comments-list'),
    path('vouchers/<int:voucher_id>/comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
    path('api/register', RegisterView.as_view(), name='register'),
    path('api/login', LoginView.as_view(), name='login'),
    path('api/logout', LogoutView.as_view(), name='logout'),
]

urlpatterns += router.urls