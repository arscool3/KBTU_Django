from django.http import HttpResponse
from django.shortcuts import render

from .forms import addPostForm
from .models import *

# Create your views here.



def addposts(request):
    if request.method == "POST":
        form = addPostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            raise Exception(f"Some Exception {form.errors}")
        return HttpResponse(f'OK, Post was created')

    return render(request, 'app/index.html', {'form': addPostForm(), 'posts': Post.objects.all().order_by('-id')})
