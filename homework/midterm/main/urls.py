
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
	path('',main,name="main"),
    path('<int:product_id>/', product_details, name="product_details"),
	path('add/<int:product_id>/',add,name="add"),
	path('cart',cart,name="cart"),
	path('increase/<int:cart_id>/<int:product_id>/',increase,name="increase"),
	path('decrease/<int:cart_id>/<int:product_id>/',decrease,name="decrease"),
	path('checkout',checkout,name='checkout'),
	path('checkoutcont/<int:order_id>/',check_continue,name="checkoutcont"),
	path('orders/',orders_list,name="order_list"),
	path('order/<int:order_id>/',order_detail,name="order_detail")
]
