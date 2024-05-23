from django.db import models

class ProductManager(models.Manager):
    def expensive_products(self):
        return self.filter(price__gt=100)

    def cheap_products(self):
        return self.filter(price__lte=100)

class CategoryManager(models.Manager):
    def category_with_most_products(self):
        from django.db.models import Count
        return self.annotate(num_products=Count('product')).order_by('-num_products').first()

    def category_with_least_products(self):
        from django.db.models import Count
        return self.annotate(num_products=Count('product')).order_by('num_products').first()
