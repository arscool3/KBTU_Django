from django.db import models


class BasicInfo(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ваше имя')
    email = models.EmailField(max_length=100, verbose_name='Ваш Email')

    def __str__(self):
        return self.name
