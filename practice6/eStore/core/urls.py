from django.urls import path
from core import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('categories/', views.category_list.as_view()),
    path('categories/<int:category_id>/', views.category_details.as_view()),
    path('categories/<int:category_id>/products', views.product_list_by_category.as_view()),

    path('products/<int:product_id>/',views.product_details.as_view()),
    path('products/', views.ProductPriceListAPIView.as_view()),
    # path('products/', views.product_details.as_view()),

    path('search/',views.search.as_view()),

    path('cartItem', views.get_cartItem.as_view()),
    path('cartItem/<int:cartItem_id>', views.cartItem_details.as_view()),
    path('cart', views.get_cart.as_view()),
    path('user', views.get_User.as_view()),
    path('signupClient', views.create_User.as_view()),
    path('signupStore', views.create_Store.as_view()),

    


    path('login', obtain_jwt_token),

    
  
    

]