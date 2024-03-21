from datetime import datetime, timezone

from django import template
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def bold(value):
    print("bold")
    return mark_safe(f"<b>{value}</b>")

@register.filter
def adorable_date(timestamp):
    date_object = datetime.fromisoformat(timestamp[:-1]).replace(tzinfo=timezone.utc)
    print(date_object)
    formatted_date = date_object.strftime("%B %d, %Y, %I:%M %p")
    return formatted_date