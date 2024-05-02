from django.db import models


class NSFWManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_adult=True)