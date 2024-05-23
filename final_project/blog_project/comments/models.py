from django.db import models
from posts.models import *
from users.models import *


class Comment(models.Model):
    blog = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)

    def __str__(self):
        return f"Комментарий от {self.user.email} для {self.blog.title}"