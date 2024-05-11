from django import template
from django.db.models import Q
from .models import Booking

register = template.Library()

@register.filter
def filter_bookings(bookings, user):
    return bookings.filter(user=user)

@register.filter
def filter_bookings_by_theme(bookings, theme):
    return bookings.filter(theme=theme)