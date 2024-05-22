from django.contrib.auth import authenticate
from rest_framework import permissions, status, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import *


class UserViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['destroy', 'update', 'partial_update']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    @action(methods=['post'], detail=False)
    def register(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginViewSet(mixins.RetrieveModelMixin,
                   GenericViewSet):
    serializer_class = LoginSerializer

    @action(methods=['post'], detail=False)
    def login(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class LikeViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_permissions(self):
        if self.action in ['create', 'destroy', 'update', 'partial_update']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
#
#
# class ProfileView(APIView):
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     authentication_classes = [SessionAuthentication]
#
#     def get(self, request):
#         try:
#             user = request.user
#             serializer = self.serializer_class(user)
#             return Response(serializer.data)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
#
#
# class RegisterView(APIView):
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#     authentication_classes = [SessionAuthentication]
#
#     # def post(self, request):
#     #     serializer = UserSerializer(data=request.data)
#     #     if serializer.is_valid():
#     #         user = serializer.save()
#     #         if user:
#     #             token, created = Token.objects.get_or_create(user=user)
#     #             return Response({'token': token.key}, status=status.HTTP_201_CREATED)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @login_required
# def profile(request):
#     user = request.user
#     return render(request, 'profile.html', {'user': user})
#
#
# def register(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST, request.FILES)
#         if form.is_valid():
#             user = form.save()
#             user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
#             if user is not None:
#                 login(request, user)
#                 return redirect('profile')
#     else:
#         form = UserForm()
#     return render(request, 'register.html', {'form': form})
#
#
# def logIn(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('profile')
#             else:
#                 return render(request, 'login.html', {'form': form, 'error_message': 'Invalid credentials'})
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})
#
#
# def logOut(request):
#     logout(request)
#     return redirect('users_default')
#
#
# class UserView(View):
#     def get(self, request):
#         users = User.objects.all()
#         return render(request, 'users.html', {'users': users})
#
#     #@login_required
#
#
#
# class CategoryView(View):
#     def get(self, request):
#         categories = Category.objects.all()
#         return render(request, 'categories.html', {'categories': categories})
#
#     @login_required
#     def post(self, request):
#         # Handle POST request for category creation
#         pass
#
#
# class PostView(View):
#     def get(self, request):
#         posts = Post.objects.all()
#         return render(request, 'posts.html', {'posts': posts})
#
#     @login_required
#     def post(self, request):
#         # Handle POST request for creating a new post
#         pass
#
#
# class CommentView(View):
#     def get(self, request):
#         comments = Comment.objects.all()
#         return render(request, 'comments.html', {'comments': comments})
#
#     @login_required
#     def post(self, request):
#         # Handle POST request for creating a new comment
#         pass
#
#
# class LikeView(View):
#     def get(self, request):
#         likes = Like.objects.all()
#         return render(request, 'likes.html', {'likes': likes})
#
#     @login_required
#     def post(self, request):
#         # Handle POST request for creating a new like
#         pass
#
#
# class ChatView(View):
#     def get(self, request):
#         chats = Chat.objects.all()
#         return render(request, 'chats.html', {'chats': chats})
#
#     @login_required
#     def post(self, request):
#         # Handle POST request for creating a new chat
#         pass
#
#
# class MessageView(View):
#     def get(self, request):
#         messages = Message.objects.all()
#         return render(request, 'messages.html', {'messages': messages})
#
#     @login_required
#     def post(self, request):
#         # Handle POST request for creating a new message
#         pass
#
#
# @login_required
# def create_category(request):
#     if request.method == 'POST':
#         form = CategoryForm(request.POST)
#         if form.is_valid():
#             category = form.save()
#             return redirect('categories')  # Redirect to author detail view
#     else:
#         form = CategoryForm()
#     return render(request, 'create_category.html', {'form': form})
#
#
# @login_required
# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save()
#             return redirect('posts')  # Redirect to author detail view
#     else:
#         form = PostForm()
#     return render(request, 'create_post.html', {'form': form})
#
#
# @login_required
# def create_comment(request):
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save()
#             return redirect('comments')  # Redirect to author detail view
#     else:
#         form = CommentForm()
#     return render(request, 'create_comment.html', {'form': form})
#
#
# @login_required
# def create_like(request):
#     if request.method == 'POST':
#         form = LikeForm(request.POST)
#         if form.is_valid():
#             like = form.save()
#             return redirect('likes')  # Redirect to author detail view
#     else:
#         form = LikeForm()
#     return render(request, 'create_like.html', {'form': form})
#
#
# @login_required
# def create_chat(request):
#     if request.method == 'POST':
#         form = ChatForm(request.POST)
#         if form.is_valid():
#             chat = form.save()
#             return redirect('chats')
#     else:
#         form = ChatForm()
#     return render(request, 'create_chat.html', {'form': form})
#
#
# @login_required
# def create_message(request):
#     if request.method == 'POST':
#         form = MessageForm(request.POST)
#         if form.is_valid():
#             message = form.save()
#             return redirect('messages')
#     else:
#         form = MessageForm()
#     return render(request, 'create_message.html', {'form': form})
#
#
# class CategoriesWithPostsView(View):
#     def get(self, request):
#         categories = Category.objects.get_with_posts()
#         return render(request, 'categories.html', {'categories': categories})
#
#
# def latest_comments(request):
#     comments = Comment.objects.get_latest_comments()
#     return render(request, 'comments.html', {'comments': comments})
#
#
# def chats_by_member(request, id):
#     chats = Chat.objects.get_chats_by_member(id)
#     return render(request, 'chats.html', {'chats': chats})
#
#
# @login_required
# def update_post(request, id):
#     post = Post.objects.get(pk=id)
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('posts')  # Redirect to category list view
#     else:
#         form = PostForm(instance=post)
#     return render(request, 'update_post.html', {'form': form})
#
#
# @login_required
# def delete_post(request, id):
#     post = Post.objects.get(pk=id)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('category_list')  # Redirect to category list view
#     return render(request, 'delete_post.html', {'post': post})