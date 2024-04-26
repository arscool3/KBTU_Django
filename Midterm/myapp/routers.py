from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'likes', LikeViewSet, basename='likes')
router.register(r'chats', ChatViewSet, basename='chats')
router.register(r'messages', MessageViewSet, basename='messages')
