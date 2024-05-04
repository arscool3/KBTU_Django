# tasks.py
import dramatiq
from dramatiq.brokers.redis import RedisBroker

# Create a Redis broker instance
broker = RedisBroker(host="localhost", port=6379)

# Set the broker for Dramatiq
dramatiq.set_broker(broker)

@dramatiq.actor
def send_email_task(recipient, subject, message):
    print(f"Sending email to {recipient} with subject '{subject}':")
    print(message)
