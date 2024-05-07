# blog/views.py
from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm


def posts_list(request):
    posts = Post.objects.all()
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts_list')
    return render(request, 'blog/posts_list.html', {'posts': posts, 'form': form})


def comments_list(request):
    comments = Comment.objects.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comments_list')
    return render(request, 'blog/comments_list.html', {'comments': comments, 'form': form})
