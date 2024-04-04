from django.urls import path

from . import views

from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ItemDetailAPIView, ItemListAPIView, ItemReviewDetailAPIView, ItemReviewListAPIView, ItemViewSet, ItemReviewViewSet


app_name = 'item'

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'reviews', ItemReviewViewSet, basename='review')

urlpatterns = router.urls

# urlpatterns = [
#     path('', views.items, name='items'),
#     path('new/', views.new, name='new'),
#     path('<int:pk>/', views.detail, name='detail'),
#     path('<int:pk>/delete/', views.delete, name='delete'),
#     path('<int:pk>/edit/', views.edit, name='edit'),
#     path('<int:pk>/write-review/', views.write_review, name='write_review'),
#     path('category/<int:category_id>/', views.CategoryItemListView.as_view(), name='category_items'),
#     path('items/', ItemListAPIView.as_view(), name='item-list'),
#     path('items/<int:pk>/', ItemDetailAPIView.as_view(), name='item-detail'),
#     path('reviews/', ItemReviewListAPIView.as_view(), name='review-list'),
#     path('reviews/<int:pk>/', ItemReviewDetailAPIView.as_view(), name='review-detail'),
# ]
