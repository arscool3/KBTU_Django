from django.shortcuts import render, redirect
from papers.models import Paper
from .forms import CommentForm


# Get

def all_comments(request, paper_id):
    paper = Paper.objects.get(id=paper_id)
    comments = paper.comments.all()
    return comments
# Post

def add_comment(request, paper_id):
    paper = Paper.objects.get(id=paper_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.paper = paper
            comment.user = request.user.account
            comment.save()
            return redirect('paper_detail', paper_id=paper_id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'paper': paper})



