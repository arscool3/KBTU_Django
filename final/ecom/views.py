from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, decorators, logout
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import status, generics, viewsets
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .permissions import CustomPermission
from .renderers import UserRenderer
from .serializers import *
from .models import *
from final.celery import send_notification


class UserRegistrationAPIView(APIView):
    renderer_classes = (UserRenderer,)
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserRenderer,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        user = request.data

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        user_id = serializer.data.get('id')
        send_notification(user_id, 'Welcome back,' + username)

        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomPermission,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.seller = request.user
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "true", "data": {"product": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "false", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        search_param = request.GET.get("search")
        products = self.get_queryset()

        if search_param:
            products = products.filter(name__icontains=search_param)

        serializer = self.serializer_class(products, many=True)
        print(serializer.data)
        return render(request, 'product.html', {'products': serializer.data})


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomPermission,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "true", "data": {"category": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "false", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        search_param = request.GET.get("search")
        categories = self.get_queryset()

        if search_param:
            categories = categories.filter(name__icontains=search_param)

        serializer = self.serializer_class(categories, many=True)
        return render(request, 'categories.html', {'categories': serializer.data})


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.author = request.user
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "true", "data": {"comment": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "false", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        search_param = request.GET.get("search")
        comments = self.get_queryset()

        if search_param:
            comments = comments.filter(content__icontains=search_param)

        serializer = self.serializer_class(comments, many=True)
        return Response({
            "success": "true",
            "comments": serializer.data
        }, status=status.HTTP_200_OK)


class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.user = request.user
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "true", "data": {"like": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "false", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        search_param = request.GET.get("search")
        likes = self.get_queryset()
        serializer = self.serializer_class(likes, many=True)
        return Response({
            "success": "true",
            "likes": serializer.data
        }, status=status.HTTP_200_OK)


class ProductLikesList(generics.ListAPIView):
    serializer_class = LikeSerializer

    def get_queryset(self):
        product_id = self.kwargs['pk']
        return Like.objects.filter(product_id=product_id)

class ProductCommentsList(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        product_id = self.kwargs['pk']
        return Comment.objects.filter(product_id=product_id)

class NotificationsViewSet(viewsets.ModelViewSet):
    permission_classes = (CustomPermission,)
    serializer_class = NotificationSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.user = request.user
        if serializer.is_valid():
            serializer.save()
            return Response({"success": "true", "data": {"Notification": serializer.data}}, status=status.HTTP_201_CREATED)
        else:
            return Response({"success": "false", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def list(self, request, *args, **kwargs):
        notifications = Notification.objects.filter(user=request.user)
        serializer = self.serializer_class(notifications, many=True)
        return Response({
            "success": "true",
            "notifications": serializer.data,
            "count": notifications.count()
        }, status=status.HTTP_200_OK)

