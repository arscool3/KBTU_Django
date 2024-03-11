
from django.contrib import admin
from django.urls import path, include
from main.views import get_products, sort_by_category, get_prod, login_user, logout_user, signup_user, addProduct, addShop, get_shops_by_city, order_prods_by_price, order_shops_budget, addCart

urlpatterns = [
    path('', get_products, name='main'),
    path('categories', sort_by_category, name='sort_by_category'),
    path('product', get_prod, name="get_product"),
    path('login_user', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('signup', signup_user, name='signup'),
    path('add_product', addProduct, name='add_product'),
    path('add_shop', addShop, name='add_shop'),
    path('shop_cities', get_shops_by_city, name='get_shops_by_city'),
    path('products_by_price', order_prods_by_price, name='order_prods_by_price'),
    path('shops_budget', order_shops_budget, name='order_shops_budget'),
    path('add_cart', addCart, name='add_cart')

]