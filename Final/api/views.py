from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK
from rest_framework.views import APIView
from .models import *
from .serializers import *


# Create your views here.
class CheckView(APIView):
    permission_classes = [IsAuthenticated]

    def index(request):
        return HttpResponse("Hello Azizbek")


class ProductByIdView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        prod = Product.objects.filter(id=id).first()
        serializer = ProductSerializer(prod)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        prod = Product.objects.filter(id=id).first()
        serializer = ProductSerializer(prod, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        else:
            return serializer.errors

    def delete(self, request, id):
        prod = Product.objects.filter(id=id).first()
        prod.delete()
        return Response({'msg': 'deleted'}, status=status.HTTP_200_OK)


class ProductsByCategoryView(APIView):
    def get(self, request, id):
        # Получаем продукты по категории
        products = Product.objects.filter(category__id=id)
        product_serializer = ProductSerializer(products, many=True)
        return Response(product_serializer.data, status=HTTP_200_OK)

    def post(self, request, id):
        category = Category.objects.filter(id=id).first()
        product = Product(
            name=request.data["name"],
            small_descr=request.data["small_descr"],
            description=request.data["description"],
            price=request.data["price"],

        )
        product.save()
        category.products.add(product)
        return Response(status=HTTP_201_CREATED)


class CategoryByIdView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        cat = Category.objects.filter(id=id).first()
        serializer = CategorySerializer(cat)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        cat = Category.objects.filter(id=id).first()
        serializer = CategorySerializer(cat, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        else:
            return serializer.errors

    def delete(self, request, id):
        cat = Category.objects.filter(id=id).first()
        cat.delete()
        return Response({'msg': 'deleted'}, status=status.HTTP_200_OK)


class ProductsView(APIView):
    def get(self, request):
        prod = Product.objects.all()
        serializer = ProductSerializer(prod, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data)


class CategoriesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        cat = Category.objects.all()
        serializer = CategorySerializer(cat, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data)


@api_view(('GET',))
def top_ten_productsByPrice(request):
    if request.method == 'GET':
        prod = Product.objects.order_by('-price')[:10]
        data = {'products': list(prod.values())}
        return Response(data)
    else:
        return Response({'error': 'Invalid request method'})


@api_view(('GET',))
def top_ten_products_byId(request):
    if request.method == 'GET':
        prod = Product.objects.order_by('id')
        data = {'products': list(prod.values())}
        return Response(data)
    else:
        return Response({'error': 'Invalid request method'})


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            UserSerializer(user, context=self.get_serializer_context()).data,
        )


class OrderListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class OrderDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        order = Order.objects.get(pk=pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class OrderProductListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order_products = OrderProduct.objects.all()
        serializer = OrderProductSerializer(order_products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class OrderProductDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        order_product = OrderProduct.objects.get(pk=pk)
        serializer = OrderProductSerializer(order_product)
        return Response(serializer.data)

    def put(self, request, pk):
        order_product = OrderProduct.objects.get(pk=pk)
        serializer = OrderProductSerializer(order_product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        order_product = OrderProduct.objects.get(pk=pk)
        order_product.delete()
        return Response(status=204)
