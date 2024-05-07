from django.urls import path
from . import views

urlpatterns = [
    # 6 GET Endpoints
    path('product-list/', views.get_product_list, name='product_list'),
    path('product-detail/<str:product_name>/', views.get_product_detail, name='product_detail'),
    path('user-orders/', views.get_user_orders, name='user_orders'),
    path('category-list/', views.category_list, name='category_list'),
    path('expensive-product-list/', views.get_expensive_product_list, name='expensive_product_list'),
    path('category-detail/<str:category_name>/', views.category_detail, name='category_detail'),

    # 6 POST Endpoints
    path('create-product/', views.create_product, name='create_product'),
    path('create-order/', views.create_order, name='create_order'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('process-payment/<int:order_id>/', views.process_payment, name='process_payment'),
    path('update-user-profile/', views.update_user_profile, name='update_user_profile'),
    path('create-category/', views.create_category, name='create_category'),
]
