from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# noinspection PyUnresolvedReferences
from api.models.userlist import UserList

@receiver(post_save, sender=User)
def create_user_wishlists(sender, instance, created, **kwargs): #keywordsargument
    if created:
        UserList.objects.create(user=instance, name=f'Reading')
        UserList.objects.create(user=instance, name=f'Read')
        UserList.objects.create(user=instance, name=f'Favorites')
        UserList.objects.create(user=instance, name=f'Planned')
        UserList.objects.create(user=instance, name=f'Abandoned')
