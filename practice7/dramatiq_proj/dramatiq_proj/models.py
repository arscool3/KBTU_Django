# models.py
from django.db import models

class Feedback(models.Model):
    content = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)
