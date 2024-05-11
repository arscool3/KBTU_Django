from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model


from .forms import *
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

    if request.method == 'POST':
        form = addCommentForm(request.POST)
        if form.is_valid():
            try:
                form.instance.user = request.user
                form.instance.post = Post.objects.get(id = p_id)
                form.save()
                return redirect('postpage', p_id)
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = addCommentForm()

    return render(request, 'app/post.html', {'P': P, 'Im': Im, 'coms': comments, 'form1': form})


def groups(request):
    Groups = Group.objects.all()
    return render(request, 'app/groups.html', {'Groups': Groups})


def group(request, g_id):
    posts = Post.objects.getGroupPosts(g_id)
    g = Group.objects.get(id=g_id)

    return render(request, 'app/group.html', {'Posts': posts, 'group': g})

def people(request):
    User = get_user_model()
    people = User.objects.all()
    return render(request, 'app/people.html', {'People': people})

def getUserPage(p_id):
    posts = Post.objects.getPersonPosts(p_id)
    user = UserInfo.objects.getinfo(p_id)

    return {'Posts': posts, 'user': user}


def person(request, p_id):
    if(p_id == request.user.id):
        return redirect('mypage')
    else:
        data = getUserPage(p_id)
        return render(request, 'app/profil.html', data)


def mypage(request):
    data = getUserPage(request.user.id)

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)

        if post_form.is_valid() and image_form.is_valid():
            post_form.instance.user = request.user
            post_instance = post_form.save()

            image_form.instance.post = post_instance
            image_form.save()
            return redirect('admin:app_image_changelist')
    else:
        post_form = PostForm()
        image_form = ImageForm()

    data['post_form'] = post_form
    data['image_form'] = image_form
    data['is_me'] = True

    return render(request, 'app/profil.html', data)


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