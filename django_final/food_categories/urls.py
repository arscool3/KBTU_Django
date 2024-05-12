from rest_framework.routers import DefaultRouter

from food_categories.views import FoodCategoryViewSet

router = DefaultRouter()

router.register(r"food_category", FoodCategoryViewSet)

urlpatterns = router.urls
