import dramatiq


@dramatiq.actor
def send_email(to, subject, body):
    print(f"Sending email to: {to}, Subject: {subject}, Body: {body}")


@dramatiq.actor
def test(title):
    print("test for test")
    print(f"Adding book {title}")
