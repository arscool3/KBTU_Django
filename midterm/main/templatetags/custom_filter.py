from django import template

register = template.Library()

@register.filter
def all_upper(value: str) -> str:
  return value.upper()

@register.filter
def sort_books_by_name(books):
  return sorted(books, key=lambda book: book.title)
