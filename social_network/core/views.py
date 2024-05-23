from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import *
from .models import *
from core.tasks import send_email_task
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse

from .renderers import UserJSONRenderer
from .serializers import (
    LoginSerializer, RegistrationSerializer, UserSerializer,
)


class RegistrationAPIView(APIView):
    renderer_classes = (UserJSONRenderer,)
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    serializer_celery = CeleryTaskSerializer
    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        email = serializer.data.get('email')
        result = send_email_task.delay('Subject', 'Welcome to network', [email])
        celery_task_data = {
            'id': result.id,
            'user': user.pk,
            'task_name': 'Registration Email'
        }
        celery_serializer = self.serializer_celery(data=celery_task_data)
        celery_serializer.is_valid(raise_exception=True)
        celery_serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return [IsAuthenticated()]

    def create(self, request, *args, **kwargs):
        # Проверка наличия данных в запросе
        if 'content' not in request.data:
            return Response({'error': 'Content field is required'}, status=status.HTTP_400_BAD_REQUEST)
        content = request.data['content']
        post = Post(author=request.user, content=content)
        post.save()
        serializer = self.get_serializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        posts = self.get_queryset()
        serializer = self.get_serializer(posts, many=True)
        return TemplateResponse(request, 'posts_list.html', {'posts': serializer.data})


class PostDetailViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    def get(self, request, post_id):
        try:
            post = Post.objects.get(pk=post_id)
            serializer = PostSerializer(post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, post_id):
        post = self.get_post(post_id)
        if not post:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post_id):
        try:
            post = Post.objects.get(pk=post_id)
            post.delete()
            return Response("deleted", status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)


class LikePostAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, post_id):
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({'error': 'You already liked this post'}, status=status.HTTP_400_BAD_REQUEST)
        like = Like(user=request.user, post=post)
        like.save()
        return Response({'message': 'Post liked successfully'}, status=status.HTTP_201_CREATED)


class DislikePostAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def post(self, request, post_id):
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
        try:
            like = Like.objects.get(user=request.user, post=post)
            like.delete()
            return Response({'message': 'Like removed successfully'}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({'error': 'You have not liked this post yet'}, status=status.HTTP_400_BAD_REQUEST)

class FollowUser(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FollowSerializer

    def get(self, request):
        current_user = request.user
        followers = Follow.objects.filter(following=current_user)  # Заменяем user на current_user
        serializer = self.serializer_class(followers, many=True)  # Заменяем comments на followers
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, user_id):
        current_user = request.user
        user_to_follow = get_object_or_404(User, pk=user_id)
        if Follow.objects.filter(follower=current_user, following=user_to_follow).exists():
            return Response({'message': 'You are already following this user'}, status=status.HTTP_400_BAD_REQUEST)

        data = {
            "follower": current_user.pk,
            "following": user_to_follow.pk
        }
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CreateComment(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer
    def get(self, request, post_id):
        comments = Comment.objects.filter(post=post_id)
        serializer = self.serializer_class(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, post_id):
        author = request.user
        comment = request.data.get('content')
        post = get_object_or_404(Post, pk=post_id)
        data = {
            "author": author.pk,
            "post": post.pk,
            "comment": comment,
        }
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)