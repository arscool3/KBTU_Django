from celery import shared_task
from django.core.mail import send_mail
from .models import UserProfile, Novel

@shared_task
def send_new_novel_notification(novel_id):
    novel = Novel.objects.get(id=novel_id)
    subject = f"New Novel Added: {novel.title}"
    message = f"A new novel titled '{novel.title}' by {novel.author} has been added to our collection.\n\nSummary:\n{novel.summary}"
    from_email = 'no-reply@example.com'
    recipient_list = [user.user.email for user in UserProfile.objects.all()]

    send_mail(subject, message, from_email, recipient_list)