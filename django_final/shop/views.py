from django.shortcuts import render, redirect, HttpResponse
from django.http import Http404, JsonResponse
from rest_framework.response import Response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout, decorators, forms
from .forms import RegistrationForm,ProductForm
from django.contrib.auth.models import User
from rest_framework.decorators import api_view,authentication_classes, permission_classes, action
from .models import Product,Brand,Category,Seller,Order,OrderItem
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer, SellerSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from decimal import Decimal
from rest_framework import status
from django.db import IntegrityError
from .tasks import send_email



# authorization
def home(request):
    return render(request, 'home.html')


def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            raise Exception(f"some errors {form.errors}")
    return render(request, 'index.html', {'form': given_form()})

def register_view(request):
    return render(request, 'register.html', {'form':RegistrationForm})


def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
            except Exception:
                return HttpResponse("something is not ok")
                
            return redirect('home')
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'login.html', {'form': forms.AuthenticationForm()})


#model
@api_view(['GET'])
def products_list(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products, many=True)
    return render(request, 'products_list.html', {'products_data': serializers.data})

@api_view(['GET'])
def products_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    serializer = ProductSerializer(product)
    return render(request, 'products_detail.html', {'product_data': serializer.data})


@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def order_list(request):
    if request.method == 'GET':
        try:
            orders = OrderItem.objects.filter(order__user=request.user)
            serializer = OrderItemSerializer(orders, many=True)
            return Response(serializer.data)
            #return render(request, 'order_list.html', {'orders_data': serializer.data})
        except Exception as e:
            return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    if request.method == 'POST':
        user = request.user
        product_id = request.data.get('product_id')
        send_email.send(user.id) 
        try:
            if not product_id:
                return Response({'message': 'Product ID is missing.'}, status=status.HTTP_400_BAD_REQUEST)

            product = Product.objects.get(id=product_id)
            order = Order.objects.create(user=user, total_price=0) 
            OrderItem.objects.create(order=order, product=product, price=product.price, quantity=1)
            
            return Response({'message': 'This product was added successfully.'}, status=status.HTTP_201_CREATED)

        except Product.DoesNotExist:
            return Response({'message': 'Invalid product ID.'}, status=status.HTTP_400_BAD_REQUEST)
            
        except IntegrityError:
            return Response({'message': 'Failed to create order. Please try again later.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
#ViewSet
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=['get'])
    def products_by_category(self, request):
        category_id = request.query_params.get('category_id')
        if not category_id:
            return Response({'message': 'Category ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        category = get_object_or_404(Category, pk=category_id)
        category_products = Product.objects.filter(category=category)
        serializer = self.get_serializer(category_products, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def products_by_brand(self, request):
        brand_id = request.query_params.get('brand_id')
        if not brand_id:
            return Response({'message': 'Brand ID is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        brand = get_object_or_404(Brand, pk=brand_id)
        brand_products = Product.objects.filter(brand=brand)
        serializer = self.get_serializer(brand_products, many=True)
        return Response(serializer.data)

class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


def send_email_view(request):
    if request.method == 'POST':
        to_email = request.POST.get('to_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_email.send(to=to_email, subject=subject, message=message)

        return HttpResponse("Email sent successfully!") 
    else:
        return render(request, 'email_template.html')