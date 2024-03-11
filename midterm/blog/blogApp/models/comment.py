from django.db import models
from django.contrib.auth import get_user_model
from blogApp.models import Post


User = get_user_model()

class Comment(models.Model):
    text_comments = models.TextField('Текст комментария ', max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.OneToOneField(Post, on_delete=models.CASCADE, primary_key=True)

    def __str__(self) -> str:
        return f"{self.text_comments}"