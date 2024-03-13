from .models import *
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import Http404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework_jwt.utils import jwt_decode_handler
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def category_products(request, id):
    category = Category.objects.get(id=id)
    products = Product.objects.filter(category=category)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist as e:
        return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    serializer = CategorySerializer(category)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def create_product(request):
    decoded = jwt_decode_handler(request.META["HTTP_AUTHORIZATION"])
    req_data = {
        "name": request.data.get('name'),
        "image": 'NO IMAGE',
        "status": request.data.get('status'),
        "category_id": request.data.get('category'),
        "price": request.data.get('price'),
        "description": request.data.get('description'),
        "user_id": decoded["user_id"]
    }

    form = Product(**req_data)
    product = form.save()
    return Response(product, status=status.HTTP_200_OK)

class ProductsAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductDetailAPIView(APIView):
    def get_object(self, id):
        try:
            return Product.objects.get(id=id)
        except Product.DoesNotExist as e:
            raise Http404

    def get(self, request, id=None):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
