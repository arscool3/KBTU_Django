from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # GET
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),  # GET
    path('category/', CategoryView.as_view(), name='category'),  # GET
    path('accounts/profile/', UserProfileView.as_view(), name='user_profile'),  # GET
    path('cart/', CartView.as_view(), name='cart'),  # GET, POST
    path('login/', CustomLoginView.as_view(), name='login'),  # POST
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # POST
    path('signup/', CustomSignUpView.as_view(), name='signup'),  # POST
    path('orders/', OrderView.as_view(), name='orders'),  # GET

    #DRF
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('user-profiles/', UserProfileListCreate.as_view(), name='user-profile-list-create'),
    path('order-items/', OrderItemListCreate.as_view(), name='order-item-list-create'),
    path('cart-items/', CartItemListCreate.as_view(), name='cart-item-list-create'),
]

#  POST requests
#  Login, Logout, Register, Remove from cart, Clear cart, Create order
#  GET requests
#  Home, Product Details, Category Details, Profile, Get Cart, Get Orders
