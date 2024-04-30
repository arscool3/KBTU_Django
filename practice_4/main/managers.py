from django.db import models

class CategoryManager(models.Manager):
    def expensive_categories(self):
        return self.filter(product__price__gte=100)

class ProductManager(models.Manager):
    def popular_products(self):
        return self.annotate(num_orders=models.Count('order')).order_by('-num_orders')

