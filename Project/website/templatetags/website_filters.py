from django import template
import datetime

register = template.Library()


# Custom Date Format Filter
@register.filter(name='custom_date_format')
def custom_date_format(value, arg='%Y-%m-%d'):
    """Formats a datetime object to a string based on a given format."""
    try:
        return value.strftime(arg)
    except AttributeError:
        return ''


# Content Teaser Filter
@register.filter(name='content_teaser')
def content_teaser(value, words=100):
    """Returns the first 'words' number of words from a text."""
    words_list = value.split()[:words]
    return ' '.join(words_list) + '...'
