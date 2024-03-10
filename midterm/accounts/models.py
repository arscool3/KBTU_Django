from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Account(User):
    pass

class PaperShelf(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='paper_shelve')
    papers = models.ManyToManyField('papers.Paper')

    def __str__(self):
        return f"{self.user.username}'s Paper Shelf"

@receiver(post_save, sender=Account)
def create_paper_shelf(sender, instance, created, **kwargs):
    if created:
        PaperShelf.objects.create(user=instance)
