from django.contrib.auth.models import User
from django.db import models

class ItemManager(models.Manager):
    def get_available_items(self):
        return self.filter(is_sold=False)

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ItemManager()
    
    def __str__(self):
        return self.name

class ItemReview(models.Model):
    item = models.OneToOneField(Item, related_name='review', on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.IntegerField()

class ItemDetail(models.Model):
    item = models.OneToOneField(Item, related_name='detail', on_delete=models.CASCADE)
    specifications = models.TextField()