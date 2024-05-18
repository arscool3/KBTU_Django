import dramatiq

from dramatiq.brokers.redis import RedisBroker
from dramatiq.results import Results
from dramatiq.results.backends.redis import RedisBackend
# from app.emails import send_password_email 
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.emails import send_password_email
from app.config.config import sender_email, sender_password

REDIS_URL = "redis://:123456@localhost:6379/0"

redis_broker = RedisBroker()
result_backend = RedisBackend(url=REDIS_URL)
redis_broker.add_middleware(Results(backend=result_backend))

dramatiq.set_broker(redis_broker)


@dramatiq.actor()
def generate_and_send_password_email(email, password):
    send_password_email(sender_email, sender_password, email, password)


