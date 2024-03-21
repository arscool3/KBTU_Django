from django.shortcuts import render
from blogApi.models.category import Category
from blogApi.models.post import Post
from blogApi.forms.postForm import PostForm
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
