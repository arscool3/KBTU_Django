from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_email_task

def my_view(request):
    """
    Example view demonstrating calling a Dramatiq task.
    """
    # Example usage of the task
    subject = "Hello"
    message = "This is a test email."
    recipient_list = ['recipient@example.com']
    
    # Call the task
    send_email_task.send(subject, message, recipient_list)
    
    # Your view logic continues...
    return HttpResponse("Task to send email queued successfully!")
