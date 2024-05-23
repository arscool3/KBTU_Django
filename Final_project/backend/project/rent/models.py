from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=250)
    img = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'image':self.image
        }


class Product(models.Model):
    STATUS = (
        ('free', 'not booked'),
        ('not free', 'booked')
    )

    name = models.CharField(max_length=250, default='')
    image = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=250, default="free", choices=STATUS)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return '%s (%s)' % (self.name, self.category)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'category': self.category.name,
            'status': self.status,
            'description': self.description,
            'price': self.price
        }

class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

