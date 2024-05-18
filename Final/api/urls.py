from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from .views import *

urlpatterns = [
    path('main/', mainPage, name='main-page'),#get
    path('user/login/', CustomLoginView.as_view(template_name="login.html"), name='login-user'),#post
    path('user/register/', register, name='register-user'), #post
    path('user/logout/<str:username>/', LogoutViewCustom.as_view(), name="logout-user"), #get
    path('user/<str:username>/', find_user_by_username), #get

    path('products/', list_of_products), #get
    path('product/<int:id>/', get_the_product),#get
    path('product/<int:id>/ratings/', product_ratings), #get, #post

    path('product/<int:id>/commentaries/', comments_by_product), #get
    path('user/<str:username>/commentaries/<int:productId>/', comment_the_product_by_user),  # post

    path('user/<str:username>/basket/', order_of_the_user), #get, post
    path('user/<str:username>/basket/delete/<int:productId>/', delete_order), #post

    path('types/', list_of_types), #get
    path('types/create/', create_type), #post
    path('sorts/', list_of_sorts), #get

]