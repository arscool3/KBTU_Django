# tasks.py
import dramatiq
from .models import Feedback

@dramatiq.actor
def process_feedback(feedback_id):
    feedback = Feedback.objects.get(id=feedback_id)
    # Do some processing here, for example, sending an email notification
    feedback.processed = True
    feedback.save()
