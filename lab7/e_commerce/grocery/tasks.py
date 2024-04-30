# my_app/tasks.py

import dramatiq
from django.core.mail import send_mail
from django.contrib.auth.models import User

@dramatiq.actor
def send_welcome_email(user_id):
    user = User.objects.get(id=user_id)
    subject = 'Welcome to our site!'
    message = f'Hi {user.username}, welcome to Almaty'
    from_email = 'Sula@gmail.com'
    to_email = [user.email]
    send_mail(subject, message, from_email, to_email)
