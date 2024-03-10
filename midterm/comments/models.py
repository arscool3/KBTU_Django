from django.db import models
from accounts.models import Account
from papers.models import Paper

class Comment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
