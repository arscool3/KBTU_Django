from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()


    def __str__(self):
        return self.title