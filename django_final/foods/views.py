from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from foods.models import Food
from foods.serializers import FoodSerializer
from utils.permissions import IsManager


class FoodViewSet(ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    # permission_classes = (IsManager, )

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["^name"]

    def get_queryset(self):
        category = self.request.query_params.get("category")
        if category:
            return Food.objects.filter(category=category)
        return super().get_queryset()
