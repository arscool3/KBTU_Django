from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .forms import UserForm, SuperuserCreationForm
from .serializers import *
from .models import *
# Create your views here.

#----------------------DONE-------------------------------
@api_view(['GET'])
def mainPage(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            context = {}
            return render(request, "main.html", context)
        return redirect("login-user")


class LogoutViewCustom(View):
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            logout(request)
        except Exception as e:
            return JsonResponse({'error': str(e)})
        return JsonResponse({'success': 'logged out'})

class CustomLoginView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('main-page')

def register(request):
    if request.method == 'POST':
        form = SuperuserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-user')  # Redirect to login page after creating superuser
    else:
        form = SuperuserCreationForm()
    return render(request, 'register.html', {'form': form})

@api_view(['GET'])
def list_of_products(request):
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return render(request, 'main.html', {'products': serializer.data})

@api_view(['GET'])
def get_the_product(request, id):
    try:
        product = Product.objects.get(id=id)
        print(product)
    except Product.DoesNotExist as e:
        return HttpResponse("Product not found.", status=404)

    serializer = ProductSerializer(product)
    return render(request, 'product.html', {'product': serializer.data})

@api_view(['GET'])
def list_of_types(request):
    if request.method == 'GET':
        type = Type.objects.all()
        serializer = TypeSerializer(type, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def create_type(request):
    if request.method == 'POST':
        serializer = TypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_of_sorts(request):
    if request.method == 'GET':
        sort = Sort.objects.all()
        serializer = SortSerializer(sort, many=True)
        return Response(serializer.data)

@api_view(['POST'])
def comment_the_product_by_user(request, username, productId):
    try:
        user = User.objects.get(username=username)
        print(user.__str__())
    except User.DoesNotExist as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    try:
        product = Product.objects.get(id=productId)
    except Product.DoesNotExist as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Error posting comment"}, status=status.HTTP_406_NOT_ACCEPTABLE)

@api_view(['GET'])
def comments_by_product(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return Response({'error': 'Product not Found'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        comments = product.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_comment_of_a_user(request, productId, userId):
    try:
        product = Product.objects.get(id=productId)
    except:
        return Response({'error': 'Product not Found'}, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        comments = Commentary.objects.filter(user__id=userId, product__id=productId)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def product_ratings(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        ratings = product.rating.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    try:
        if request.method == 'POST':
            ratings = Rating.objects.get(user__username=request.data.get('user'), product__id=id)
            serializer = RatingSerializer(instance=ratings, data=request.data)
            if serializer.is_valid():  # only when data ?= data. in the create method we are providing only data
                 serializer.save(product=product)
                 return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({"error": "failed to update"}, status=status.HTTP_400_BAD_REQUEST)
    except Rating.DoesNotExist as e:
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():  # only when data ?= data. in the create method we are providing only data
            serializer.save(product=product)
            return Response(serializer.data)
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


@api_view(['GET'])
def find_user_by_username(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = {'id': user.id, 'username': user.username.__str__(), 'email':user.email.__str__()}
        return Response(data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def order_of_the_user(request, username):
    try:
        user = User.objects.get(username=username)
        print(user.__str__())
    except User.DoesNotExist as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        order = user.orders.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        order = user.orders.filter(products__id=request.data.get('products'))
        if(len(order) > 0):
            return Response({"error": "Already in basket"}, status=status.HTTP_400_BAD_REQUEST)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error": "Error posting order"}, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(['GET', 'POST'])
def delete_order(request, username, productId):
    try:
        user = User.objects.get(username=username)
        print(user.__str__())
    except User.DoesNotExist as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    try:
        product = Product.objects.get(id=productId)
    except Product.DoesNotExist as e:
        return Response({"error": str(e)}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'POST':
        order = Order.objects.filter(user__username =username, products__id=productId)
        order.delete()
        return Response({"delete": "Deleted successfully"})

#------------------------------------------------------------

