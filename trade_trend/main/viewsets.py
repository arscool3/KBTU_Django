from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from .models import User, Product, Category, Review, Order, Cart, Notification
from .serializers import UserSerializer, ProductSerializer, CategorySerializer, ReviewSerializer, OrderSerializer, CartSerializer, NotificationSerializer
from .tasks import notify_user_of_order
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

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

    def get_queryset(self):
        queryset = Product.objects.all()
        category_id = self.request.query_params.get('category', None)
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset
    
    @action(detail=True, renderer_classes=[TemplateHTMLRenderer])
    def detail(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        return Response(request, {'product': product}, template_name='product_detail.html')


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def create_order(self, request, pk=None):
        product = self.get_object()
        order, created = Order.objects.get_or_create(user=request.user, status='Pending')
        if created:
            cart_item, _ = Cart.objects.get_or_create(user=request.user, product=product)
            cart_item.quantity = 1
            cart_item.save()
        serializer = self.get_serializer(order)
        return Response(serializer.data)
    
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def add_to_cart(self, request, pk=None):
        product = self.get_object()
        cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        serializer = self.get_serializer(cart_item)
        return Response(serializer.data)
    
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def list(self, request, *args, **kwargs):
        queryset = Notification.objects.filter(user=request.user)
        serializer = NotificationSerializer(queryset, many=True)
        return Response(serializer.data)