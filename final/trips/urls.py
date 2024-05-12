from django.urls import path

from rest_framework import routers
from .views import CategoryViewSet, TripViewSet, UserViewSet, CommentViewSet, FavoriteViewSet, OrderViewSet, ProfileViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import categories_list, categories_trips, trips_list, \
    trips_detail, favorite_list,home, \
    profile, register_view, logout_view, favorite_list, get_favorites, login_view, add_comment, get_comments, \
    delete_comment, edit_comment

from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'trips', TripViewSet)
router.register(r'users', UserViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'favorites', FavoriteViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'user_profile', ProfileViewSet)

urlpatterns = [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('', home, name='home'),
    path('categories_list/', categories_list, name="category_list"),
    path('categories/<int:category_id>/', categories_trips, name='category_detail'),
    path('trips_list/', trips_list, name="trips_list"),
    path('trips/<int:trip_id>/', trips_detail, name='trips_detail'),
    path('api/register', register_view, name='register'),
    path('api/login', login_view, name='login'),
    path('api/logout', logout_view, name='logout'),
    path('profile/', profile, name='profile'),
    path('favorite_list/', favorite_list, name='favorite_list'),
    path('get_favorites/', get_favorites, name='get_favorites'),
    path('trips/<int:trip_id>/add_comment/', add_comment, name='add_comment'),
    path('get_comments/', get_comments, name='get_comments'),
    path('comments/<int:comment_id>/edit/', edit_comment, name='edit_comment'),
    path('comments/<int:comment_id>/delete/', delete_comment, name='delete_comment'),

]

urlpatterns += router.urls
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)