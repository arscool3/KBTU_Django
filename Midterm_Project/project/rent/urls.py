from django.urls import path
import rest_framework_jwt.views
from .views import *
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('categories/', category_list),
    path('categories/<int:id>/', category_detail),
    path('categories/<int:id>/products/', category_products),
    path('products/', ProductsAPIView.as_view()),
    path('product/', create_product),
    path('products/<int:id>/', ProductDetailAPIView.as_view()),
    path('login/', obtain_jwt_token)
]