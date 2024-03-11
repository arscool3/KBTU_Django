from http.client import HTTPResponse
from django.shortcuts import render, redirect
from blogApp.models.post import Post
from blogApp.forms.postForm import PostForm

# Create your views here.

def get(request, post_id = None):
    if post_id:
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return HTTPResponse("no post")
        return render("index.html", post=post)
    post = Post.objects.all()
    
    return render("index.html", post=post)
def post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
    return redirect('')
        