from django.shortcuts import render, redirect, get_object_or_404
from .models import Paper, Category
from accounts.models import PaperShelf
from .forms import *
from comments.views import all_comments

# GET
def home(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def papers_by_category(request, category_id):
    papers = Paper.objects.papers_by_category(category_id)
    return render(request, 'papers_list.html', {'papers': papers})

def paper_detail(request, paper_id):
    paper = get_object_or_404(Paper, pk=paper_id)
    comments = all_comments(request, paper_id)
    return render(request, 'paper.html', {'paper': paper, 'comments': comments})


def search_by_tags(request):
    if request.method == 'GET':
        form = TagSearchForm(request.GET)
        if form.is_valid():
            selected_tags = form.cleaned_data['tags']
            if selected_tags:
                papers = Paper.objects.filter(tags__in=selected_tags).distinct()
            else:
                papers = Paper.objects.all()
            return render(request, 'papers_list.html', {'papers': papers})
    else:
        form = TagSearchForm()
    return render(request, 'search_by_tags.html', {'form': form})


# POST
def add_to_shelf(request, paper_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            paper_shelf = PaperShelf.objects.get(user=request.user.account)
            paper_shelf.papers.add(paper_id)
            return redirect('paper_detail', paper_id=paper_id)
        else:
            return redirect('login')
    return redirect('home')


def create_paper(request):
    if request.method == 'POST':
        form = PaperForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PaperForm()
    return render(request, 'create_paper.html', {'form': form})



def create_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TagForm()
    return render(request, 'create_tag.html', {'form': form})


def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm()
    return render(request, 'create_category.html', {'form': form})
