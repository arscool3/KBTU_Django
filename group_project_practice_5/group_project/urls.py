"""group_project_practice_5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book_store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', views.get_books, name='get_books'),
    path('books/<int:book_id>/', views.get_book, name='get_book'),
    path('authors/', views.get_authors, name='get_authors'),
    path('authors/<int:author_id>/', views.get_author, name='get_author'),
    path('publishers/', views.get_publishers, name='get_publishers'),
    path('publishers/<int:publisher_id>/', views.get_publisher, name='get_publisher'),
    path('create_book/', views.create_book, name='create_book'),
    path('update_book/<int:book_id>/', views.update_book, name='update_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
    path('create_author/', views.create_author, name='create_author'),
]
