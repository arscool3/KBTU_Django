from django.db import models
#import django.db.models import Q

class Base(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True

class City(Base):
    city_code = models.CharField(max_length=5)

class CustomerQuerySet(models.QuerySet):
    def filter_name_starting_with_D(self):
        return self.filter(name = r'K.*')

class Customer(Base):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    objects = CustomerQuerySet.as_manager()

class Seller(Base):
    city_name = models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)

class Item(Base):
    item_id = models.IntegerField()
    cost = models.FloatField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    amount = models.IntegerField()

class Orders():
    order_id = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    Item = models.ForeignKey(Item, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)

#