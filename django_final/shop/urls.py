from django.urls import path, include
from rest_framework import routers
from .views import home,  register_view, login_view, logout_view, products_list,products_detail,order_list ,BrandViewSet, CategoryViewSet, ProductViewSet, SellerViewSet, OrderViewSet, OrderItemViewSet,send_email_view

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'sellers', SellerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'orderitems', OrderItemViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('register', register_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('products/', products_list, name="products_list"),
    path('products/<int:product_id>/', products_detail, name='product_detail'),
    path('order_list/', order_list, name='order_list'),
    path('send-email/', send_email_view, name='send_email'),
]
urlpatterns += router.urls