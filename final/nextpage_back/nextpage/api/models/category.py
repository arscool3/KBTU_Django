from django.db import models


class Category(models.Model):
    def __str__(self):
        return f'{self.name}'
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=255)




    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }