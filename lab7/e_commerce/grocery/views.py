from collections import OrderedDict
from django.shortcuts import render

# Create your views here.
from .tasks import send_welcome_email
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Order, OrderItem, Customer
from .serializers import OrderItemSerializer, ProductSerializer, OrderSerializer, CustomerSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import authenticate



class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductDetailView(APIView):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

class OrderListView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        orders = Order.objects.filter(customer=request.user.customer)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

class OrderDetailView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request, order_id):
        order = Order.objects.get(id=order_id)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

class CustomerProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self, request):
        customer = request.user.customer
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

class SearchProductsView(APIView):
    def get(self, request):
        query = request.query_params.get('query', '')
        products = Product.objects.filter(name__icontains=query)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# POST Views
class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def post(self, request):
        user = request.user
        customer = user.customer
        product_id = request.data.get('product_id')
        quantity = int(request.data.get('quantity', 1))

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product does not exist"}, status=status.HTTP_404_NOT_FOUND)

        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

        if not created:
            order_item.quantity += quantity
            order_item.save()
        else:
            order_item.quantity = quantity
            order_item.save()

        serializer = OrderItemSerializer(order_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        user = request.user
        customer = user.customer

        # Retrieve the active order for the customer
        try:
            order = Order.objects.get(customer=customer, complete=False)
        except Order.DoesNotExist:
            return Response({"error": "No active order found for the customer"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the order has any items
        if order.orderitem_set.count() == 0:
            return Response({"error": "Cannot place an order with no items"}, status=status.HTTP_400_BAD_REQUEST)

        # Calculate total order amount
        total_amount = order.get_cart_total()

        # Perform payment processing (e.g., charging the customer)

        # Update order status to complete
        order.complete = True
        order.save()

        # Return order details
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class RegisterCustomerView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        address = request.data.get('address')
        phone_number = request.data.get('phone_number')

        if not username or not email or not password:
            return Response({"error": "Username, email, and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
            return Response({"error": "Username or email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Create the customer
        customer = Customer.objects.create(user=user, address=address, phone_number=phone_number)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        serializer = CustomerSerializer(customer)
        return Response({"customer": serializer.data, "access_token": access_token}, status=status.HTTP_201_CREATED)
    

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response({"access_token": access_token}, status=status.HTTP_200_OK)
    

class UpdateCustomerProfileView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        customer = request.user.customer
        serializer = CustomerSerializer(instance=customer, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddProductView(APIView):
    permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

# views.py


def register_user(request):
    # Your user registration logic here
    user = User.objects.create(username='Sultan', email='Sula@gmail.com')
    
    # Enqueue the send_welcome_email task
    send_welcome_email.send(user.id)
