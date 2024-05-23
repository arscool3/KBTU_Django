from django.urls import path

from .views import (
    LoginAPIView,
    RegistrationAPIView,
    UserRetrieveUpdateAPIView,
    PostViewSet,
    PostDetailViewSet,
    LikePostAPIView,
    DislikePostAPIView,
    FollowUser,
    CreateComment,
)
app_name = 'core'
urlpatterns = [
    # Update
    path('user/', UserRetrieveUpdateAPIView.as_view()),

    # Регистрация пользователя
    path('users/', RegistrationAPIView.as_view()),

    # login
    path('users/login/', LoginAPIView.as_view()),

    # Получение детальной информации о публикации
    path('users/<user_id>/follow/', FollowUser.as_view()),

    # Получение списка подписчиков
    path('users/followers/', FollowUser.as_view()),

    # Создание новой публикации / список публикаций
    path('posts/', PostViewSet.as_view({'post': 'create', 'get': 'list'})),

    # Получение детальной информации о публикации
    path('posts/<post_id>/', PostDetailViewSet.as_view({'get': 'get', 'delete': 'delete'})),

    # Поставить лайк на публикацию
    path('posts/<post_id>/like/', LikePostAPIView.as_view()),

    # Убрать лайк с публикации
    path('posts/<post_id>/dislike/', DislikePostAPIView.as_view()),

    # написать коммент на публикацию
    path('posts/<post_id>/comment/', CreateComment.as_view()),
]