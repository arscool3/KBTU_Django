from django.urls import path

from .views import (
    LoginAPIView,
    RegistrationAPIView,
    UserRetrieveUpdateAPIView,
    PostViewSet,
    PostDetailViewSet,
    LikePostAPIView,
    DislikePostAPIView,
)
app_name = 'core'
urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),

    # path('users/<user_id>/follow/', ),

    # Создание новой публикации / список публикаций
    path('posts/', PostViewSet.as_view({'post': 'create', 'get': 'list'})),

    # Получение детальной информации о публикации
    path('posts/<post_id>/', PostDetailViewSet.as_view({'get': 'get', 'delete': 'delete'})),

    # Удаление публикации

    # Поставить лайк на публикацию
    path('posts/<post_id>/like/', LikePostAPIView.as_view()),

    # Убрать лайк с публикации
    path('posts/<post_id>/dislike/', DislikePostAPIView.as_view()),

    # path('posts/<post_id>/comment/'),

]