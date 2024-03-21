from django.shortcuts import render, HttpResponse
from manager_app.forms import *

# Create your views here.
def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'form.html', {'form': AuthorForm()})

def add_topic(request):
    if request.method == 'POST':
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'form.html', {'form': TopicForm()})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'form.html', {'form': PostForm()})

def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'form.html', {'form': CommentForm()})


def get_all_posts(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        return render(request, 'index.html', {'iterable': posts})
    
def get_all_topics(request):
    if request.method == 'GET':
        topics = Topic.objects.all()
        return render(request, 'index.html', {'iterable': topics})

def get_posts_by_topic(request):
    if request.method == 'POST':
        form = TopicSelectionForm(request.POST)
        if form.is_valid():
            selected_author = form.cleaned_data['author']
            posts = Post.objects.get__post_by_topic(author=selected_author)
            return render(request, 'index.html', {'posts': posts})
    else:
        form = TopicSelectionForm()
    return render(request, 'form.html', {'form': form})

