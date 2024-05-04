from django.shortcuts import render
from django.http import HttpResponse
from django import template

register = template.Library()


@register.filter
def PutPriorityLevel(value):
    if value == 1:
        return "Very High"
    elif value == 2:
        return "High"
    else:
        return "Normal"