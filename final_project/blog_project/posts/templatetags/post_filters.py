from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter(name='highlight')
def highlight(value, arg):
    # Highlights all occurrences of arg in value by wrapping them in HTML <mark> tags
    return format_html(value.replace(arg, f'<mark>{arg}</mark>'))

@register.filter(name='truncate_n_words')
def truncate_n_words(value, arg):
    # Truncates the text after a specified number of words
    words = value.split()[:int(arg)]
    return ' '.join(words) + '...'
