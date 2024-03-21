from django.db import models

class First_Manager(models.Manager):
    def get_customer_by_email(self, email):
        return self.get(email=email)
    
    def get_orders_by_user(self, username):
        return self.filter(username=username)


class Second_Manager(models.Manager):
    def get_all_products_by_categoryname(self, category_name):
        return self.filter(category=category_name)
    
    def get_expensive_products(self):
        return self.filter(price__gte=100)