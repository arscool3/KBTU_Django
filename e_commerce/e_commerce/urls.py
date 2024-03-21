"""
URL configuration for e_commerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from grocery import views

# urlpatterns = [
#     # GET Endpoints
#     path('products/', views.ProductListView.as_view(), name='product-list'),
#     path('products/<int:product_id>/', views.ProductDetailView.as_view(), name='product-detail'),
#     path('orders/', views.OrderListView.as_view(), name='order-list'),
#     path('orders/<int:order_id>/', views.OrderDetailView.as_view(), name='order-detail'),
#     path('customer/profile/', views.CustomerProfileView.as_view(), name='customer-profile'),
#     path('search/products/', views.SearchProductsView, name='search-products'),

#     # POST Endpoints
#     path('cart/add/', views.AddToCartView, name='add-to-cart'),
#     path('order/place/', views.PlaceOrderView, name='place-order'),
#     path('customer/register/', views.RegisterCustomerView, name='register-customer'),
#     path('customer/login/', views.LoginView, name='login'),
#     path('customer/update-profile/', views.UpdateCustomerProfileView, name='update-customer-profile'),
#     path('product/add/', views.AddProductView, name='add-product'),
# ]
from django.urls import path
# from . import views

urlpatterns = [
    # GET Endpoints
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:product_id>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('orders/<int:order_id>/', views.OrderDetailView.as_view(), name='order-detail'),
    path('customer/profile/', views.CustomerProfileView.as_view(), name='customer-profile'),
    path('search/products/', views.SearchProductsView.as_view(), name='search-products'),

    # POST Endpoints
    path('cart/add/', views.AddToCartView.as_view(), name='add-to-cart'),
    path('order/place/', views.PlaceOrderView.as_view(), name='place-order'),
    path('customer/register/', views.RegisterCustomerView.as_view(), name='register-customer'),
    path('customer/login/', views.LoginView.as_view(), name='login'),
    path('customer/update-profile/', views.UpdateCustomerProfileView.as_view(), name='update-customer-profile'),
    path('product/add/', views.AddProductView.as_view(), name='add-product'),
]
