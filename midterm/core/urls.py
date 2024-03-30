from django.contrib import admin
from django.urls import path

from core.views import *
from core.drf_views import *
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('check/', check_view, name='check'),
    path('logout/', logout_view, name='logout'),
    path('category/<int:id>/', category_detail_view, name='category_detail'), # пример пути для просмотра категории
    path('product/<int:id>/', product_detail_view, name='product_detail'), # пример пути для просмотра продукта
    path('order/<int:id>/', order_detail_view, name='order_detail'), # пример пути для просмотра заказа
    path('profile/', user_profile_view, name='user_profile'), # пример пути для просмотра профиля пользователя
    path('cart/', cart_view, name='cart'), # пример пути для просмотра корзины
    path('review/<int:id>/', review_view, name='review'), # пример пути для просмотра отзыва
    path('add_to_cart/', add_to_cart_view, name='add_to_cart'),  # Путь для добавления в корзину
    path('make_order/', make_order_view, name='make_order'),  # Путь для создания заказа
    path('products/', get_all_products, name='all_products'),  # Путь для создания заказа
    path('add_to_oder/<int:order_id>', add_product_to_order , name = 'add_product_to_order'),
    path('add_profile_info/', add_profile_info , name = 'add_profile_info'),
    path('get_cart_info/', cart_detail , name = 'cart_detail'),
    path('products/drf', get_all_products_drf, name='all_products_drf')
]