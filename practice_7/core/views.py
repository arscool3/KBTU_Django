from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import CosmeticProduct
from .serializers import CosmeticProductSerializer
# Create your views here.

class CosmeticProductViewSet(viewsets.ModelViewSet):
    queryset = CosmeticProduct.objects.all()
    serializer_class = CosmeticProductSerializer

    def create(self, request, id=None):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            notify_user_about_new_cosmetic_product.send(serializer.instance.id)  
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
