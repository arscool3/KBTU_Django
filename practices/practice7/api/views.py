from django.shortcuts import render, redirect
from .models import  BlogPost
from .tasks import send_new_blog_post_notification

from .forms import SubscriberForm, BlogPostForm


def create_subscriber(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogpost-list')
    else:
        form = SubscriberForm()
    return render(request, 'create_subscriber.html', {'form': form})

def create_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            send_new_blog_post_notification(post.id)
            return redirect('blogpost-detail', pk = post.id)
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})


def blogpost_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def blogpost_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})

