from rest_framework.viewsets import ModelViewSet

from food_categories.models import FoodCategory
from food_categories.serializers import FoodCategorySerializer
from utils.permissions import IsManager


class FoodCategoryViewSet(ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer
    permission_classes = (IsManager, )
