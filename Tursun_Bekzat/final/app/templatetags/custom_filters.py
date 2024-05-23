import bleach
from django import template
import markdown
import datetime


register = template.Library()


@register.filter(name='markdown')
def markdown_format(text):
    return markdown.markdown(text)


@register.filter(name='tag_list')
def tag_list(tags):
    return ', '.join([tag.name for tag in tags])


ALLOWED_TAGS = [
    'p', 'b', 'i', 'u', 'strong', 'em', 'br', 'a', 'ul', 'ol', 'li', 'blockquote', 'code', 'pre'
]


@register.filter(name='safe_html')
def safe_html(text):
    return bleach.clean(text, tags=ALLOWED_TAGS, strip=True)


@register.filter(name='format_date')
def format_date(value):
    return value.strftime('%B %d, %Y')

