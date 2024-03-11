from django.db import models

class CategoryManager(models.Manager):
    def get_categories_with_products_count(self):
        return self.annotate(num_products=models.Count('product')).filter(num_products__gt=0)

class ProductManager(models.Manager):
    def get_products_in_category(self, category_name):
        return self.filter(category__name=category_name)