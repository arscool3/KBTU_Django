from django.urls import include, path
from comments.viewsets import CommentViewSet
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', get_all_comments),
    path('create', create_comment),
    path('update/pk', update_comment),
    path('delete/pk', delete_comment),

    # Viewsets
    path('', include(router.urls)),
]