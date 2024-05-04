import dramatiq

from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

@dramatiq.actor
def send_welcome_email(user_id):
    user = User.objects.get(pk=user_id)
    send_mail(
        subject="Welcome to MyBlog!",
        message="Hi %s, thanks for joining MyBlog!" % user.username,
        from_email="noreply@myblog.com",
        recipient_list=[user.email],
        fail_silently=False,
    )