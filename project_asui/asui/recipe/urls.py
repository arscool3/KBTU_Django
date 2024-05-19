from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.cbv import IngredientViewSet, RecipeViewSet, DirectionViewSet, MeasurementUnitViewSet, MeasurementQuantityViewSet, RecipeIngredientViewSet, ReviewViewSet
from .views.fbv import recipe_rating


router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'directions', DirectionViewSet)
router.register(r'measurement-units', MeasurementUnitViewSet)
router.register(r'measurement-quantities', MeasurementQuantityViewSet)
router.register(r'recipe-ingredients', RecipeIngredientViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:recipe_id>/rating/', recipe_rating),
    # maybe shoplist
]
