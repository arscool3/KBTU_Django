from django import template
from ..models import Book

register = template.Library()

@register.filter(name='filter_books_by_genre')
def filter_books_by_genre(genre):
    return Book.objects.filter(genre__name=genre)
