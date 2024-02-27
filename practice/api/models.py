from unicodedata import name
from django.db import models

# Create your models here.
class Base(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return name
    
    class Meta:
        abstract = True



class ProductQuerySet(models.QuerySet):
    def used_product(self):
        return self.filter(used= True)
    def not_used_product(self):
        return self.filter(used=False)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def usedItems(self):
        return self.get_queryset().used_product()
    def not_usedItems(self):
        return self.get_queryset().not_used_product()


class CartQuerySet(models.QuerySet):
    def repeated(self):
        return self.filter(repeated=True)
    
    def not_repeated(self):
        return self.filter(repeated=False)

class CartManager(models.Manager):
    def get_queryset(self):
        return CartQuerySet(self.model, using=self._db)
    def repeatedItems(self):
        return self.get_queryset().repeated()
    
    def notRepeatedItems(self):
        return self.get_queryset().not_repeated()
class Product(Base):
    price = models.IntegerField()
    used = models.BooleanField()
    objects = ProductManager()
    
    def __str__(self) -> str:
        return f"{super().name}, {self.price}"


class Category(Base):
    name = models.CharField(max_length=200)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.name}, {self.products}"

class CartItem(models.Model):
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    qunatity = models.IntegerField(default=1)
    repeated = models.BooleanField(default=False)


