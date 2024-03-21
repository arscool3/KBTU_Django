from django.urls import path
from . import views

urls = [
    path('categories/', views.get_all_categories, name='category_list'),
    path('products/', views.get_all_products, name='products_list'),
    path('productbycategory/', views.get_all_products_by_categoryname, name='category_name'),
    path('product_details/', views.get_product_by_name, name='product_details'),
    path('orders/', views.get_orders_by_user, name='orders'),
    path('customer/', views.get_customer_by_email, name='customer'),
]