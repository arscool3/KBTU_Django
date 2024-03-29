from django.shortcuts import render
from blogApi.filters.post_filter import post_filter
from blogApi.models.category import Category
from blogApi.models.post import Post
from blogApi.forms.post_form import PostForm
from django.contrib.auth import decorators

@decorators.login_required(login_url='login')
def get(request): 
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})


@decorators.login_required(login_url='login')
def post(request):
    form = PostForm(request.POST)
    categories = Category.objects.all()
    if form.is_valid():
        form.save()

    return render(request, 'addPost.html',
                  {'form':form, "categories":categories})

@decorators.login_required(login_url='login')
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post_detail.html', {'post':post})

@decorators.login_required(login_url='login')
def post_list(request):
    f = post_filter(request.GET, queryset=Post.objects.all())
    return render(request, 'index.html', {'filter': f})