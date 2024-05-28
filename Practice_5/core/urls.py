from django.urls import path
from . import views

urlpatterns = [
    path('shops/', views.shop_list, name='shop_list'),
    path('sections/', views.section_list, name='section_list'),
    path('producers/', views.producer_list, name='producer_list'),
    path('goods/', views.goods_list, name='goods_list'),
]