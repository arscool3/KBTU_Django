from django.urls import path
from rest_framework import routers

from .views import *

router = routers.SimpleRouter()
router.register(r"posts", PostViewSet)
router.register(r"userinfos", UserInfoViewSet)
router.register(r"users", UserViewSet)
router.register(r"images", ImageViewSet)
router.register(r"comments", CommentViewSet)
router.register(r"likes", LikeViewSet)
router.register(r"groups", GroupViewSet)
router.register(r"subscriptions", SubscriptionViewSet)

urlpatterns = [] + router.urls