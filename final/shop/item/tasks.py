import dramatiq
from django.core.mail import send_mail
from django.contrib.auth.models import User


@dramatiq.actor
def send_new_item_notification(user_id, item_name):
    user = User.objects.get(id=user_id)
    send_mail(
        'New Item Available',
        f'Hello {user.username},\n\nA new item "{item_name}" has been added to the store.',
        'ayanjkeewow@gmail.com',
        [user.email],
        fail_silently=False,
    )