from django.db import models
from blogApi.models.post import Post
from django.contrib.auth.models import User
class Comments(models.Model):
    text_comments = models.TextField('текст комментария', max_length=2000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User,default=None, on_delete = models.CASCADE)
    def __str__(self) -> str:
        return f'{self.text_comments}'

