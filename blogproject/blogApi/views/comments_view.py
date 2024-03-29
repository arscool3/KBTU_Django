from django.shortcuts import render, redirect
from django.views.generic.base import View
from blogApi.models.comments import Comments
from blogApi.forms.comment_form import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required(login_url='login'),name='post')
class AddComments(View):

    def post(self,request,pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.author = request.user
            form.save()
        return redirect(f'/{pk}')