from django.urls import path
from .views import *

urlpatterns = [
    path("category/add", add_category, name='add_category'),
    path("categories/",get_category_list, name='categories'),
    path("products/add", add_product, name="add_product"),
    path("products",get_products, name='products'),
    path("products/<str:category_name>/",get_product_list_by_category, name='products_by_category'),
    path("product/<int:product_id>/",get_product_details, name='product'),

    path('register/', register_view, name='register'),
    path("logout/", logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('check/', check_view, name='check'),

    path("user/",get_user, name='user'),

    path("carts/",get_cart, name='cart'),
    path("cartitems/",get_cart_items, name='cartitems'),
    path("addtocart/", add_cart_items, name="addtocart")





]