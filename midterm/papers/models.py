from django.db import models
from accounts.models import Account

class Paper(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    #tags = models ADD Later
    authors = models.ManyToManyField(Account, related_name='papers')
    created_at = models.DateTimeField(auto_now_add=True)
    #tags = models.ManyToManyField(Tag, related_name = 'papers')
    #category = models.OneToOneField(Category, related_name = 'papers')

    def __str__(self):
        return self.title
