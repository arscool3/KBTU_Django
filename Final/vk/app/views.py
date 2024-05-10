from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model


from .forms import RegisterUserForm
from .models import *
from django.contrib.auth import login, logout
# Create your views here.

def postspage(request):
    Posts = Post.objects.all()
    Images = Image.objects
    return render(request, 'app/posts.html', {'Posts': Posts, 'Images': Images})


def postpage(request, p_id):
    P = Post.objects.get(id=p_id)
    Im = Image.objects.get(post=p_id).photo.url
    comments = Comment.objects.getPostComs(p_id)

    return render(request, 'app/post.html', {'P': P, 'Im': Im, 'coms': comments})


def groups(request):
    Groups = Group.objects.all()
    return render(request, 'app/groups.html', {'Groups': Groups})

def people(request):
    User = get_user_model()
    people = User.objects.all()
    return render(request, 'app/people.html', {'People': people})


def mypage(request):
    return render(request, 'app/profil.html', {'Products': []})


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'app/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'app/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        UserInfo.objects.just_registrated(user)
        return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('login')