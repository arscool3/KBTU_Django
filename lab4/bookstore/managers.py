from django.db import models

class ProductManager(models.Manager):
    def expensive_products(self):
        return self.filter(price__gt=100)

    def cheap_products(self):
        return self.filter(price__lte=100)

class OrderManager(models.Manager):
    def high_total_orders(self):
        return self.filter(total_price__gt=1000)

    def low_total_orders(self):
        return self.filter(total_price__lte=1000)
