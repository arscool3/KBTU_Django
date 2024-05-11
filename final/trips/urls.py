from django.urls import path

from rest_framework import routers
from .views import CategoryViewSet, TripViewSet, UserViewSet, CommentViewSet, FavoriteViewSet, OrderViewSet

from .views import categories_list, CommentsListAPIView, CommentDetailAPIView, categories_trips, trips_list, \
    trips_detail, get_favorites_by_user, favorite_list,get_favorite_by_trip,home, \
    UsersListAPIView, UsersDetailAPIView, create_comment, profile, register_view, logout_view, get_favorites_by_user, favorite_list, get_favorites, login_view

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'trips', TripViewSet)
router.register(r'users', UserViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = [
    path('', home, name='home'),
    path('categories_list/', categories_list, name="category_list"),
    path('categories/<int:category_id>/', categories_trips, name='category_detail'),
    path('trips_list/', trips_list, name="trips_list"),
    path('trips/<int:trip_id>/', trips_detail, name='trips_detail'),
    path('trips/<int:trip_id>/comments/', CommentsListAPIView.as_view(), name='comments-list'),
    path('trips/<int:trip_id>/comments/<int:pk>/', CommentDetailAPIView.as_view(), name='comment-detail'),
    path('api/register', register_view, name='register'),
    path('api/login', login_view, name='login'),
    path('api/logout', logout_view, name='logout'),
    path('trips/<int:trip_id>/comments/', create_comment, name='create_comment'),
    path('profile/', profile, name='profile'),
    path('favorite_list/', favorite_list, name='favorite_list'),
    path('get_favorites/', get_favorites, name='get_favorites'),

]

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)