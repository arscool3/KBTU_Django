from django.shortcuts import redirect, render

from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .forms import ArticleForm, DestinationForm
from .models import Article, Destination

def index(request):
  return render(request, 'index.html')
    
def create_article(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST)
    if form.is_valid():
      instance = form.save()
      return redirect('get_articles')
  else:
    form = ArticleForm()

  return render(request, 'article_form.html', {'form': form})

def get_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles.html', {'articles': articles})

def search_articles(request):
    keyword = request.GET.get('keyword')
    articles = Article.objects.filter(title__icontains=keyword)
    articles_data = [{'title': article.title, 'author': article.author} for article in articles]
    return JsonResponse(articles_data, safe=False)

def get_latest_articles(request):
    latest_articles = Article.objects.order_by('-publication_date')[:10]  # Get latest 10 articles
    latest_articles_data = [{'title': article.title, 'author': article.author} for article in latest_articles]
    return JsonResponse(latest_articles_data, safe=False)


def create_destination(request):
  if request.method == 'POST':
    form = DestinationForm(request.POST)
    if form.is_valid():
      instance = form.save()
      return redirect('get_destinations')
  else:
    form = DestinationForm()

  return render(request, 'destination_form.html', {'form': form})

def get_destinations(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations.html', {'destinations': destinations})
