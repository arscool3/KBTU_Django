import dramatiq

@dramatiq.actor
def send_email(to, subject, body):
    # Code to send email
    print(f"Sending email to: {to}, Subject: {subject}, Body: {body}")
