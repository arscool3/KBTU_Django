import dramatiq
from django.core.mail import send_mail
from django.template.loader import render_to_string

@dramatiq.actor
def send_email(to, subject, message):
    email_message = render_to_string('email_template.html', {'message': message})
    
    send_mail(subject, email_message, '	admin@example.com', [to])
    print(f"Email sent to {to} with subject: {subject}")
