from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Type(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class Sort(models.Model):
    sort = models.CharField(max_length=255)

    def __str__(self):
        return self.sort


class Category(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="categories")
    sort = models.ForeignKey(Sort, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return f"type: {self.type.__str__()}, sort: {self.sort.__str__()}"


class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f'{self.name}'


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating')
    rating = models.FloatField(default=0)

    def __str__(self):
        return f'{self.product.name}: {self.rating}'


class Commentary(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return "Comment {} by {}".format(self.created_at, self.user)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    products = models.ForeignKey(Product, related_name="orders", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.__str__()

