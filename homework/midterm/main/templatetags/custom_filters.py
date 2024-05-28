from django import template

register = template.Library()

@register.filter
def format_price(price):
    return "${:.2f}".format(price / 100)

@register.filter
def truncate_title(title, length=30):
    if len(title) > length:
        return title[:length] + "..."
    else:
        return title
