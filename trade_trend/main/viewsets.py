from django.shortcuts import render
from rest_framework import viewsets, status
from .models import User, Product, Category, Review, Order
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, ReviewSerializer, OrderSerializer
from .tasks import notify_user_of_order
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        categories = serializer.data
        return render(request, "categories.html", {"categories": categories})

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        products = serializer.data
        return render(request, "products.html", {"products":products})


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    @action(detail=True, methods=['post'])
    def add_review(self, request, pk=None):
        # custom logic for adding a review
        return Response(status=status.HTTP_201_CREATED)
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    @action(detail=False, methods=['post'])
    def create_order(self, request):
        order = Order.objects.create(user=request.user, status='Pending')
        notify_user_of_order.delay(order.id)
        return Response(status=status.HTTP_201_CREATED)