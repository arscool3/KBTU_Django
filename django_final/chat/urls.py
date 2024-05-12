from rest_framework.routers import DefaultRouter

from chat.views import *

router = DefaultRouter()

router.register(r"chat", ChatViewSet)
router.register(r"message", MessageViewSet)

urlpatterns = router.urls
