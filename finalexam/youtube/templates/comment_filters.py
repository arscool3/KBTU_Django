from django import template

register = template.Library()

@register.filter
def format_comment(comment_text):
    """Format the comment text."""
    return comment_text.upper()

@register.filter
def shorten_comment(comment_text, max_length=50):
    """Shorten the comment text to a maximum length."""
    if len(comment_text) > max_length:
        return comment_text[:max_length] + "..."
    return comment_text
