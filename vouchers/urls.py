from django.urls import path

from rest_framework import routers
from .views import CategoryViewSet, VoucherViewSet, UserViewSet, CommentViewSet, FavoriteViewSet, OrderViewSet

from .views import categories_list, CommentsListAPIView, CommentDetailAPIView, categories_vouchers, vouchers_list, \
    vouchers_detail, get_favorites_by_user, favorite_list,get_favorite_by_voucher,home, \
    UsersListAPIView, UsersDetailAPIView, create_comment, profile, register_view, login_view, logout_view

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
    path('categories_list/', categories_list, name="category_list"),
    path('categories/<int:category_id>/', categories_vouchers, name='category_detail'),
    path('vouchers_list/', vouchers_list, name="vouchers_list"),
    path('vouchers/<int:voucher_id>/', vouchers_detail, name='vouchers_detail'),
    path('vouchers/<int:voucher_id>/comments/', CommentsListAPIView.as_view(), name='comments-list'),
    path('vouchers/<int:voucher_id>/comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
    path('api/register', register_view, name='register'),
    path('api/login', login_view, name='login'),
    path('api/logout', logout_view, name='logout'),
    path('vouchers/<int:voucher_id>/comments/', create_comment, name='create_comment'),
    path('profile/', profile, name='profile'),
]

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)