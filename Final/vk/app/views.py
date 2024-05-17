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
    Im = Image.objects.getPostImage(p_id)
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


def like(request, p_id):
    Like.objects.likeDislike(request.user, p_id)
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def groups(request):
    Groups = Group.objects.all()
    if request.user.is_authenticated:
        myGroups = Group.objects.myGroups(request.user)
    else:
        myGroups = []
    return render(request, 'app/groups.html', {'Groups': Groups, 'MyGroups': myGroups})


def group(request, g_id):
    posts = Post.objects.getGroupPosts(g_id)
    g = Group.objects.get(id=g_id)

    if request.method == 'POST':
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)

        if post_form.is_valid() and image_form.is_valid():
            post_form.instance.user = request.user
            post_form.instance.group = g
            post_instance = post_form.save()

            image_form.instance.post = post_instance
            image_form.save()
    else:
        post_form = PostForm()
        image_form = ImageForm()

    context = {'Posts': posts, 'group': g, 'is_owner': g.owner == request.user,
               'post_form': post_form, 'image_form': image_form}

    return render(request, 'app/group.html', context)


def addGroup(request):
    if request.method == 'POST':
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.instance.owner = request.user
                form.save()
                return redirect('groups')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = GroupForm()

    return render(request, 'app/addPage.html', { 'title': 'Добавить Группу', 'form': form})


def SubGroup(request, g_id):
    Subscription.objects.subscribe(Group.objects.get(id=g_id), request.user)
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))

def UnsubGroup(request, g_id):
    Subscription.objects.unsubscribe(Group.objects.get(id=g_id), request.user)
    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


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
            return redirect('mypage')
    else:
        post_form = PostForm()
        image_form = ImageForm()

    data['post_form'] = post_form
    data['image_form'] = image_form
    data['is_me'] = True

    return render(request, 'app/profil.html', data)

def ChangeUserInfo(request):
    usInfo = UserInfo.objects.getinfo(request.user)
    if request.method == 'POST':
        form = UserInfoForm(request.POST, request.FILES, instance=usInfo)

        if form.is_valid():
            form.save()
            return redirect('mypage')
    else:
        form = UserInfoForm(instance=usInfo)

    return render(request, 'app/addPage.html', {'title': 'Изменить профиль', 'form': form})

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