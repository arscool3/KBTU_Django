from django import template
from datetime import datetime
register = template.Library()

@register.filter
def truncate(value, length):
    if len(value) > length:
        return value[:length] + '...'
    else:
        return value
    
@register.filter
def format_date(value, format_str='%b %d, %Y'):
    if isinstance(value, datetime):
        return value.strftime(format_str)
    return value