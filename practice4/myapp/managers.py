from django.db import models


class ProductManager(models.Manager):
    def get_products_by_category(self, category_id):
        return self.filter(category_id=category_id)

    def get_products_with_price_less_than(self, max_price):
        return self.filter(price__lt=max_price)


class OrderManager(models.Manager):
    def get_orders_by_customer(self, customer_name):
        return self.filter(customer_name=customer_name)

    def get_orders_with_total_amount_greater_than(self, min_amount):
        return self.filter(total_amount__gt=min_amount)
