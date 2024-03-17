from django.shortcuts import render

from .forms import PostForm
from .models import Post


# Create your views here.
def create_post(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form, 'posts': posts})
