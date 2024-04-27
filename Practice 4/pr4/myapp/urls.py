from django.urls import path
from .views import ProductListView, create_product , create_category , category_list , view_cart , add_to_cart, delete_from_cart

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('create-product/', create_product, name='create-product'),
    path('create-category/', create_category, name='create-category'),
    path('category-list/', category_list, name='category-list'),
    path('cart-list/', view_cart, name='view_cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('delete-from-cart/<int:cart_item_id>/', delete_from_cart, name='delete_from_cart'),
]