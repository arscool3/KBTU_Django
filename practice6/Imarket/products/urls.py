from .views import CategoryViewSet, ProductViewSet, SubCategoryViewSet
from django.urls import path

from rest_framework import routers

urlpatterns = [
    path('categories/<int:category_id>/products/',
         ProductViewSet.as_view({'get': 'get_category_products'}), name='list of category products'),
    path('categories/<int:category_id>/subcategories/',
         SubCategoryViewSet.as_view({'get': 'get_subcategories_of_category'})),
    path('categories/<int:category_id>/subcategories/<int:subcat_id>/products/',
         ProductViewSet.as_view({'get': 'get_subcategory_products'})),
    path('subcategories/<int:sabcategory_id>/name/',
         ProductViewSet.as_view({'get': 'get_subcategory_name'}),
         name='get subcategory name '),
    path('products/rating/<int:min>/',
         ProductViewSet.as_view({'get': 'get_products_min_rating'}), name='products with minimum rate'),
    path('products/<int:product_id>/put_rating/',
         ProductViewSet.as_view({'patch': 'put_rating_to_product'}), name='rate product'),
    path('popular_products/',
         ProductViewSet.as_view({'get': 'get_popular_products'}), name='sorted in desc by rating'),
    path('products/name/',
         ProductViewSet.as_view({'post': 'search_by_name'}), name='search product by name'),

    path('products/searching/<str:query>/',
         ProductViewSet.as_view({'get': 'searching'}), name='search product'),
    path('products/<int:product_id>/avg_price/',
         ProductViewSet.as_view({'get': 'get_products_avg_price'}), name='avg price'),
    path('shops/<int:shop_id>/products/',
         ProductViewSet.as_view({'get': 'get_products_of_shop'}), name='shop products')
]

r = routers.DefaultRouter()

r.register(r'products', ProductViewSet)
r.register(r'categories', CategoryViewSet)

urlpatterns += r.urls
