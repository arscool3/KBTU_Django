from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('authors/', TemplateView.as_view(template_name = 'author_list.html'), name = 'author_list'),
    path('books/', TemplateView.as_view(template_name = 'book_list.html'), name = 'book_list'),
]