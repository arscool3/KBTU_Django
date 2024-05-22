import dramatiq
from dramatiq.brokers.redis import RedisBroker
from pydantic import EmailStr
from config import Email
from ssl import create_default_context
from email.mime.text import MIMEText
from smtplib import SMTP

redis_broker = RedisBroker()
dramatiq.set_broker(redis_broker)

@dramatiq.actor
def send_registration_email(email: EmailStr):
    message = MIMEText("Accaunt with this email was created", "html")
    message["From"] = Email.USERNAME
    message["To"] = email
    message["Subject"] = "Registration complete"

    ctx = create_default_context()
    try:
        with SMTP(Email.HOST, Email.PORT) as server:
            server.starttls(context=ctx)
            server.login(Email.USERNAME, Email.PASSWORD)
            server.send_message(message)
            server.quit()
    except Exception as e:
        print(e)
