from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from main.models import Category
from main.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
  serializer_class = CategorySerializer
  queryset = Category.objects.all()
  lookup_field = 'id'