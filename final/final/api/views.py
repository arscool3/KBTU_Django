from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required, permission_required

from api.serializers import *
from core.models import *

from celery import shared_task

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    """def update(self, request, pk=None):
        if request.user:
            if request.user.id == 1:
                return super().update(self, request, pk)
            else:
                return Response(status=403)
        else:
            return Response(status=401)"""
    permission_classes = [permissions.IsAuthenticated]
    """def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]"""

class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-name')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    @action(detail=True, methods=['get'])
    def get_products_by_cat(self, request, pk=None):
        cat = self.get_object()
        prods = Product.objects.filter(category=cat.id)
        serializer = self.get_serializer(prods, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-name')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
@shared_task
def get_history_by_user_task(self, request, pk=None):
    user = self.get_object().user
    hist = HistoryItem.objects.filter(user=user)
    serializer = self.get_serializer(hist, many=True)
    return Response(serializer.data)

class HistoryItemViewSet(viewsets.ModelViewSet):
    queryset = HistoryItem.objects.all().order_by('-date')
    serializer_class = HistoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    @action(detail=True, methods=['get'])
    def get_history_by_user(self, request, pk=None):
        get_history_by_user_task(self,request,pk)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-text')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]