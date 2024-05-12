from rest_framework.routers import DefaultRouter

from foods.views import FoodViewSet

router = DefaultRouter()

router.register(r"food", FoodViewSet)

urlpatterns = router.urls
