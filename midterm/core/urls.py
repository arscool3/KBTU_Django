from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [

    path('register/', views.register_view, name='register'),

    path('login/', views.login_view, name='login'),

    path("logout/", views.logout_view, name='logout'),

    path('home/', views.HomeView.as_view(), name='home'),
    
    path('about/', views.AboutView.as_view(), name='about'),
    

    #Products
    path('products/create/', views.CreateProductView.as_view(), name='create_product'),
    
    path('products/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),
    
    path('products/<int:product_id>/update/', views.UpdateProductView.as_view(), name='update_product'),
    
    path('products/', views.ProductListView.as_view(), name='product_list'),

    #Categories
    
    path('categories/create/', views.CreateCategoryView.as_view(), name='create_category'),

    path('categories/<int:category_id>/', views.CategoryDetailView.as_view(), name='category_detail'),

    path('categories/<int:category_id>/update/', views.UpdateCategoryView.as_view(), name='update_category'),

    path('categories/', views.CategoryListView.as_view(), name='category_list'),


    # Customer urls
    path('customers/create/', views.CreateCustomerView.as_view(), name='create_customer'),
    
    path('customers/<int:customer_id>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    
    path('customers/<int:customer_id>/update/', views.UpdateCustomerView.as_view(), name='update_customer'),
    
    path('customers/', views.CustomerListView.as_view(), name='customer_list'),

    #orders

    path('orders/create/', views.CreateOrderView.as_view(), name='create_order'),
    
    path('orders/<int:order_id>/', views.OrderDetailView.as_view(), name='order_detail'),
    
    path('orders/<int:order_id>/update/', views.UpdateOrderView.as_view(), name='update_order'),
    
    path('orders/', views.OrderListView.as_view(), name='order_list'),


]