# main/templatetags/custom_filters.py

from django import template

register = template.Library()

@register.filter
def capitalize_names(student_list):
    return [name.capitalize() for name in student_list]
