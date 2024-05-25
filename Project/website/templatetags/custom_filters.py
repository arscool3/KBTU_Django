from django import template

register = template.Library()

@register.filter
def sort_chapters(chapters):
    return chapters.order_by('chapter_number')
def sort_novels(novels):
    return novels.order_by('title')