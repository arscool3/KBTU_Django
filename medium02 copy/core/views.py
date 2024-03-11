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

class HomeView(ListView):
    model = Article
    template_name = 'home.html'
    def get_queryset(self):
        # Query articles ordered by the number of likes in descending order
        return Article.objects.annotate(like_count=models.Count('like')).order_by('-like_count')[:2]

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
    return HttpResponse("You have logout")


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


# # 12 Endpoints (6 get, 6 post)
# 6post

@decorators.permission_required('core.can_add_articles', login_url='login')
def add_articles(request):
    return basic_form(request,ArticleForm)

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
    return render(request, 'article_confirm_delete.html', {'article': article})

@decorators.permission_required('core.can_add_comments', login_url='login')
def add_comments(request):
    return basic_form(request,CommentForm)

@decorators.permission_required('core.can_add_topics', login_url='login')
def add_topics(request):
    return basic_form(request,TopicForm)

@decorators.permission_required('core.can_add_readinglists', login_url='login')
def add_readinglists(request):
    return basic_form(request,ReadingListForm)

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

    return render(request, 'profile.html', {'form': form, 'creating_profile': creating_profile, 'profile': profile})

def profile(request):
    profile = request.user.profile
    follower_count = Follow.objects.filter(followed_user=profile.user).count()
    followers = Follow.objects.filter(followed_user=profile.user).select_related('follower__profile')
    articles = Article.objects.filter(author=profile.user)
    return render(request, 'profile.html', {'profile': profile, 'follower_count': follower_count, 'followers': followers, 'articles': articles})

@login_required
def add_likes(request,pk):
    article = get_object_or_404(Article, id=pk)
    already_liked = Like.objects.filter(user=request.user, article=article).exists()
    if not already_liked:      
        like = Like.objects.create(user=request.user, article=article)
        like.save()
    return redirect('likes')



@login_required
def add_follows(request, username):
    # Get the user to follow
    user_to_follow = User.objects.get(username=username)
    # Create a Follow object if it doesn't exist
    follow, created = Follow.objects.get_or_create(follower=request.user, followed_user=user_to_follow)
    return redirect('follows')


#6 get

def get_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})


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



def get_readinglists(request):

    readinglists = ReadingList.objects.get(profile__user=request.user)

    return render(request, 'readinglists.html', {'readinglists': readinglists})
