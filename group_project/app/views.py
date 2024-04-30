from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import User, Category, Post, Comment

def get_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    data = {
        'name': user.name,
        'email': user.email,
    }
    return JsonResponse(data)

def create_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user = User.objects.create(name=name, email=email)
        return JsonResponse({'message': 'User created successfully'})
    else:
        return JsonResponse({'error': 'POST method required for creating user'})

def get_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    data = {
        'name': category.name,
        'post_count': category.post_set.count(),
    }
    return JsonResponse(data)

def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category = Category.objects.create(name=name)
        return JsonResponse({'message': 'Category created successfully'})
    else:
        return JsonResponse({'error': 'POST method required for creating category'})

def get_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    data = {
        'name': post.name,
        'description': post.description,
        'text': post.text,
        'date': post.date,
        'author': post.author.name,
    }
    return JsonResponse(data)

def create_post(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        text = request.POST.get('text')
        author_id = request.POST.get('author_id')
        author = get_object_or_404(User, id=author_id)
        post = Post.objects.create(name=name, description=description, text=text, author=author)
        return JsonResponse({'message': 'Post created successfully'})
    else:
        return JsonResponse({'error': 'POST method required for creating post'})

def get_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    data = {
        'text': comment.text,
        'date': comment.date,
        'author': comment.author.name,
        'post': comment.post.name,
    }
    return JsonResponse(data)

def create_comment(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        post_id = request.POST.get('post_id')
        author_id = request.POST.get('author_id')
        post = get_object_or_404(Post, id=post_id)
        author = get_object_or_404(User, id=author_id)
        comment = Comment.objects.create(text=text, post=post, author=author)
        return JsonResponse({'message': 'Comment created successfully'})
    else:
        return JsonResponse({'error': 'POST method required for creating comment'})
