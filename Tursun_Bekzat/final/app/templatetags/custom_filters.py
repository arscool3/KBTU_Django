from django import template
import markdown

register = template.Library()


@register.filter(name='markdown')
def markdown_format(text):
    return markdown.markdown(text)


@register.filter(name='tag_list')
def tag_list(tags):
    return ', '.join([tag.name for tag in tags])