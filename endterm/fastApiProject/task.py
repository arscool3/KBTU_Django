from celery.app import Celery
from datetime import datetime
import os

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(__name__, broker=redis_url, backend=redis_url)

@celery_app.task
def reserve_ticket(ticket):
    import time
    import random
    time.sleep(random.randint(1, 5))
    return f"Succesfully reserved ticket: {ticket}"


@celery_app.task
def log_to_file(filename, message):
    with open(f"{filename}.txt", "a") as f:
        f.write(message + "\n")