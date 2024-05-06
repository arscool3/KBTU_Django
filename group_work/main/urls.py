from django.contrib import admin
from django.urls import path

from main.views import create_article, create_destination, get_articles, get_destinations, index

urlpatterns = [
  path('articles/', get_articles, name="get_articles"),
  path('create-article/', create_article, name="create_article"),
  path('destinations/', get_destinations, name="get_destinations"),
  path('create-destination/', create_destination, name="create_destination"),
  path('', index, name="index")
] 
