from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import PostForm



def list_published_posts(request):
    posts = Post.objects.get_published_posts()
    return render(request, 'posts/list.html', {'posts': posts})

def list_active_categories(request):
    categories = Category.objects.get_active_categories()
    return render(request, 'categories/list.html', {'categories': categories})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:list')
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})
