from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from .forms import *


@login_required
def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})


def logIn(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
            else:
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


class UserView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users.html', {'users': users})

    @login_required
    @csrf_exempt
    def post(self, request):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            return render(request, 'create_user.html', {'form': form})


class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'categories.html', {'categories': categories})

    @login_required
    def post(self, request):
        # Handle POST request for category creation
        pass


class PostView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'posts.html', {'posts': posts})

    @login_required
    def post(self, request):
        # Handle POST request for creating a new post
        pass


class CommentView(View):
    def get(self, request):
        comments = Comment.objects.all()
        return render(request, 'comments.html', {'comments': comments})

    @login_required
    def post(self, request):
        # Handle POST request for creating a new comment
        pass


class LikeView(View):
    def get(self, request):
        likes = Like.objects.all()
        return render(request, 'likes.html', {'likes': likes})

    @login_required
    def post(self, request):
        # Handle POST request for creating a new like
        pass


class ChatView(View):
    def get(self, request):
        chats = Chat.objects.all()
        return render(request, 'chats.html', {'chats': chats})

    @login_required
    def post(self, request):
        # Handle POST request for creating a new chat
        pass


class MessageView(View):
    def get(self, request):
        messages = Message.objects.all()
        return render(request, 'messages.html', {'messages': messages})

    @login_required
    def post(self, request):
        # Handle POST request for creating a new message
        pass


@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save()
            return redirect('categories')  # Redirect to author detail view
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts')  # Redirect to author detail view
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


@login_required
def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comments')  # Redirect to author detail view
    else:
        form = CommentForm()
    return render(request, 'create_comment.html', {'form': form})


@login_required
def create_like(request):
    if request.method == 'POST':
        form = LikeForm(request.POST)
        if form.is_valid():
            like = form.save()
            return redirect('likes')  # Redirect to author detail view
    else:
        form = LikeForm()
    return render(request, 'create_like.html', {'form': form})


@login_required
def create_chat(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            chat = form.save()
            return redirect('chats')
    else:
        form = ChatForm()
    return render(request, 'create_chat.html', {'form': form})


@login_required
def create_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            return redirect('messages')
    else:
        form = MessageForm()
    return render(request, 'create_message.html', {'form': form})


class CategoriesWithPostsView(View):
    def get(self, request):
        categories = Category.objects.get_with_posts()
        return render(request, 'categories.html', {'categories': categories})


def latest_comments(request):
    comments = Comment.objects.get_latest_comments()
    return render(request, 'comments.html', {'comments': comments})


def chats_by_member(request, id):
    chats = Chat.objects.get_chats_by_member(id)
    return render(request, 'chats.html', {'chats': chats})
