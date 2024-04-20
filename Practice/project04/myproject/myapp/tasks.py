import dramatiq

@dramatiq.actor
def send_email_task(recipient_email, message):
    print(f"Sending email to {recipient_email}: {message}")
