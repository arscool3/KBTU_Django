from django.db import models

class CategoryManager(models.Manager):
    def get_popular_categories(self):
        return self.annotate(num_products=models.Count('product')).order_by('-num_products')[:5]

    def get_category_by_name(self, name):
        return self.get(name=name)

class ProductManager(models.Manager):
    def get_expensive_products(self):
        return self.filter(price__gte=100)

    def get_products_by_category(self, category_name):
        return self.filter(category__name=category_name)