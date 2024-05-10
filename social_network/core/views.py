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

from .renderers import UserJSONRenderer
from .serializers import (
    LoginSerializer, RegistrationSerializer, UserSerializer,
)


class RegistrationAPIView(APIView):
    """
    Разрешить всем пользователям (аутентифицированным и нет) доступ к данному эндпоинту.
    """
    renderer_classes = (UserJSONRenderer,)
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    serializer_celery = CeleryTaskSerializer
    def post(self, request):
        user = request.data.get('user', {})

        # Паттерн создания сериализатора, валидации и сохранения - довольно
        # стандартный, и его можно часто увидеть в реальных проектах.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Получите адрес электронной почты нового пользователя
        email = serializer.data.get('email')
        # Здесь можно добавить логику для получения других данных пользователя,
        # если они нужны для формирования письма.

        # Отправьте задачу Celery для отправки электронного письма
        result = send_email_task.delay('Subject', 'Message', ['recipient@example.com'])
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

        # Обратите внимание, что мы не вызываем метод save() сериализатора, как
        # делали это для регистрации. Дело в том, что в данном случае нам
        # нечего сохранять. Вместо этого, метод validate() делает все нужное.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        # Здесь нечего валидировать или сохранять. Мы просто хотим, чтобы
        # сериализатор обрабатывал преобразования объекта User во что-то, что
        # можно привести к json и вернуть клиенту.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        # Паттерн сериализации, валидирования и сохранения - то, о чем говорили
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
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        # Проверка наличия данных в запросе
        if 'content' not in request.data:
            return Response({'error': 'Content field is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Получение данных из запроса
        content = request.data['content']

        # Создание новой публикации
        post = Post(author=request.user, content=content)
        post.save()

        # Сериализация созданной публикации и возврат ответа
        serializer = self.get_serializer(post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        # Получение всех публикаций из базы данных
        posts = self.get_queryset()

        # Сериализация списка публикаций и возврат ответа
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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

        # Проверка, не лайкнул ли пользователь уже этот пост
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({'error': 'You already liked this post'}, status=status.HTTP_400_BAD_REQUEST)

        # Создание нового лайка
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

        # Проверка, лайкнул ли пользователь уже этот пост
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

        # Получаем пользователя, на которого пользователь хочет подписаться
        user_to_follow = get_object_or_404(User, pk=user_id)

        # Проверяем, не подписан ли уже текущий пользователь на этого пользователя
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
        # Получаем текущего пользователя
        author = request.user
        comment = request.data.get('content')
        # Получаем пост, к которому добавляется комментарий
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