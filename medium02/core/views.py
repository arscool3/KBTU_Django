from django.contrib.auth import (
    authenticate, decorators, forms, login, logout
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import (
    HttpResponse, get_object_or_404, redirect, render
)
from core.forms import (
    ArticleForm, CommentForm, EditArticleForm, ReadingListForm, TopicForm,ProfileForm
)
from core.models import (
    Article, Comment, Follow, Like, Profile, ReadingList, Topic
)
from django.views.generic import ListView
from django.db import models
from django.contrib import messages

class HomeView(ListView):
    model = Article
    template_name = 'home.html'
def basic_form(request, given_form):
    if request.method == 'POST':
        form = given_form(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': given_form()})


def register_view(request):
    return basic_form(request, forms.UserCreationForm)

def logout_view(request):
    logout(request)
    return HttpResponse("You have logged out")


def login_view(request):
    if request.method == 'POST':
        form = forms.AuthenticationForm(data=request.POST)
        if form.is_valid():
            try:
                user = authenticate(**form.cleaned_data)
                login(request, user)
                if next := request.GET.get("next"):
                    return redirect(next)
                return HttpResponse("everything is ok")
            except Exception:
                return HttpResponse("something is not ok")
        else:
            raise Exception(f"some erros {form.errors}")
    return render(request, 'index.html', {'form': forms.AuthenticationForm()})


@decorators.login_required(login_url='login')
def check_view(request):
    if request.user.is_authenticated:
        return HttpResponse(f"{request.user} is authenticated")
    raise Exception(f"{request.user} is not authenticated")

def profile(request,username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    follower_count = Follow.objects.filter(followed_user=profile.user).count()

    articles = Article.objects.filter(author=profile.user)
    return render(request, 'profile.html', {'profile': profile, 'follower_count': follower_count,'articles': articles})
def my_profile(request):
    return redirect('profile', username=request.user.username)

def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})


# 6post

@decorators.permission_required('core.can_add_articles', login_url='login')
def add_articles(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, user=request.user)  # Pass the current user to the form
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user  # Assign the current user to the author field
            article.save()
            return redirect('articles')  # Redirect to the article list page
    else:
        form = ArticleForm(user=request.user)  # Pass the current user to the form

    return render(request, 'add_articles.html', {'form': form})

@decorators.permission_required('core.can_upd_articles', login_url='login')
def update_articles(request,pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        form = EditArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles')
    else:
        form = EditArticleForm(instance=article)
    return render(request, 'update_articles.html', {'form': form})

@decorators.permission_required('core.can_del_articles', login_url='login')
def delete_articles(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles')
    return render(request, 'delete_articles.html', {'article': article})

@decorators.permission_required('core.can_add_comments', login_url='login')
def add_comments(request):
    return basic_form(request,CommentForm)

@decorators.permission_required('core.can_add_topics', login_url='login')
def add_topics(request):
    return basic_form(request,TopicForm)


@login_required
def add_to_reading_list(request, pk):
    article = get_object_or_404(Article, pk=pk)
    reading_list, created = ReadingList.objects.get_or_create(profile=request.user.profile)
    reading_list.articles.add(article)
    messages.success(request, f'Article "{article.title}" added to your reading list.')
    return redirect('article_detail', pk=pk)

@login_required
def edit_profile(request):
    try:
        profile = request.user.profile
        creating_profile = False
    except Profile.DoesNotExist:
        profile = None
        creating_profile = True

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form, 'creating_profile': creating_profile, 'profile': profile})

@login_required
def add_likes(request,pk):
    article = get_object_or_404(Article, id=pk)
    already_liked = Like.objects.filter(user=request.user, article=article).exists()

    if already_liked:
        # User has already liked the article, so remove the like
        Like.objects.filter(user=request.user, article=article).delete()
        messages.success(request, 'You unliked the article.')
    else:
        # User hasn't liked the article yet, so add the like
        like = Like.objects.create(user=request.user, article=article)
        like.save()
        messages.success(request, 'You liked the article.')

    return redirect('article_detail', pk=pk)


@login_required
def add_comments(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article=article)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            messages.success(request, 'Your comment has been added successfully.')
            return redirect('article_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'add_comments.html', {'article': article, 'comments': comments, 'form': form})

@login_required
def add_follows(request, username):
    # Get the user to follow
    user_to_follow = User.objects.get(username=username)
    # Create a Follow object if it doesn't exist
    follow, created = Follow.objects.get_or_create(follower=request.user, followed_user=user_to_follow)
    return redirect('follows')



def get_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def get_user_articles(request, username):
    user_articles = Article.objects.filter(author__username=username)
    return render(request, 'user_articles.html', {'user_articles': user_articles, 'username': username})

def get_user_followers(request, username):
    user = get_object_or_404(User, username=username)
    user_followers = Follow.objects.filter(followed_user=user).select_related('follower__profile')
    return render(request, 'user_followers.html', {'user_followers': user_followers, 'username': username})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    like_count = Like.objects.filter(article=article).count()
    comment_count = Comment.objects.filter(article=article).count() 

    return render(request, 'article_detail.html', {'article': article, 'like_count': like_count, 'comment_count': comment_count})

def get_topics(request):
    topics =Topic.objects.all()
    return render(request, 'topics.html', {'topics': topics})


def get_profiles(request):
    profiles =Profile.objects.all()
    return render(request, 'profiles.html', {'profiles': profiles})


def get_comments(request):
    comments =Comment.objects.all()
    return render(request, 'comments.html', {'comments': comments})

def get_likes(request):
    likes=Like.objects.all()
    return render(request, 'likes.html', {'likes':likes})

def liked_users(request, pk):
    article = get_object_or_404(Article, pk=pk)
    liked_users = Like.objects.filter(article=article).values_list('user__username', flat=True)
    return render(request, 'liked_users.html', {'article': article, 'liked_users': liked_users})

def article_comments(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = Comment.objects.filter(article=article)
    return render(request, 'article_comments.html', {'article': article, 'comments': comments})

def get_readinglists(request):

    readinglists = ReadingList.objects.get(profile__user=request.user)

    return render(request, 'readinglists.html', {'readinglists': readinglists})

def articles_by_hot_topic(request):

    articles_by_hot_topic = Article.objects.by_topic('Feminism')

   
    context = {
        'articles_by_hot_topic': articles_by_hot_topic
    }

    return render(request, 'hot_topic.html', context)
