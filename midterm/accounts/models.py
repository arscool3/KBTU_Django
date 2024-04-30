from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    instance.account.save()


class PaperShelf(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='paper_shelf')
    papers = models.ManyToManyField('papers.Paper')

    def __str__(self):
        return f"{self.user.user.username}'s Paper Shelf"

@receiver(post_save, sender=Account)
def create_paper_shelf(sender, instance, created, **kwargs):
    if created:
        PaperShelf.objects.create(user=instance)
