from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, decorators, logout, forms
from django.http import JsonResponse
from core.models import Article,Comment,Follow,Like,Topic,Profile,ReadingList
from core.forms import ArticleForm,CommentForm,EditArticleForm,TopicForm,ReadingListForm

from django.contrib.auth.models import User

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

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

@login_required
def add_likes(request,pk):
    article = get_object_or_404(Article, id=pk)

    # Check if the user has already liked the article
    already_liked = Like.objects.filter(user=request.user, article=article).exists()

    if not already_liked:
        # If the user has not liked the article yet, create a new like
        like = Like.objects.create(user=request.user, article=article)
        like.save()

    # Redirect the user back to the article detail page after liking
    return redirect('likes')

"""
class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    followed_user = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.follower.username} follows {self.followed_user.username}"

"""
@login_required
def add_follows(request, username):
    # Get the user to follow
    user_to_follow = User.objects.get(username=username)
    # Create a Follow object if it doesn't exist
    follow, created = Follow.objects.get_or_create(follower=request.user, followed_user=user_to_follow)
    return redirect('follows')


#class DeletePostView(DeleteView):
#    model = Post
#    template_name = 'delete_post.html'
#    success_url = reverse_lazy('home')

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



def get_followers(request):
    follows=Follow.objects.all()
    return render(request, 'follows.html', {'follows':follows})


def get_likes(request):
    likes=Like.objects.all()
    return render(request, 'likes.html', {'likes':likes})

from django.shortcuts import render
from .models import ReadingList

def get_readinglists(request):

    readinglists = ReadingList.objects.get(profile__user=request.user)

    return render(request, 'readinglists.html', {'readinglists': readinglists})
