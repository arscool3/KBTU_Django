from django.shortcuts import render, HttpResponse
from core.forms import *
# Create your views here.
def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'form.html', {'form': AuthorForm()})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'form.html', {'form': PostForm()})


def create_story_note(request):
    if request.method == 'POST':
        form = StoryNoteForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("saved")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'form.html', {'form': StoryNoteForm()})


def create_comment(request):
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
        return render(request, 'posts.html', {
            'iterable_name': "Posts",
            'posts': posts
        })
    
def select_posts_by_author(request):
    if request.method == 'POST':
        form = AuthorSelectionForm(request.POST)
        if form.is_valid():
            selected_author = form.cleaned_data['author']
            posts = Post.objects.get_by_author(author=selected_author)
            return render(request, 'posts.html', {'posts': posts})
    else:
        form = AuthorSelectionForm()
    return render(request, 'form.html', {'form': form})

def select_comments_by_post(request):
    if request.method == 'POST':
        form = PostSelectionForm(request.POST)
        if form.is_valid():
            selected_post = form.cleaned_data['post']
            comments = Comment.objects.get_by_post(post=selected_post)
            comments = comments.get_recent()
            return render(request, 'comments.html', {'comments': comments})
    else:
        form = AuthorSelectionForm()
    return render(request, 'form.html', {'form': form})

def select_comments_by_author(request):
    if request.method == 'POST':
        form = AuthorSelectionForm(request.POST)
        if form.is_valid():
            selected_author = form.cleaned_data['author']
            comments = Comment.objects.get_by_author(author=selected_author)
            return render(request, 'comments.html', {'comments': comments})
    else:
        form = AuthorSelectionForm()
    return render(request, 'form.html', {'form': form})