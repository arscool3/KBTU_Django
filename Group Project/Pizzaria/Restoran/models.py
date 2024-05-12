from django.db import models

# Create your models here.
class common(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True


class Food(common):
    description = models.TextField(blank=True)
    cost = models.IntegerField()
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

    def getFoodData(self):
        data = [self.pk, self.name, self.description, self.cost, self.cat]
        return data

    def changedescription(self, new):
        self.description = new

    def changeCost(self, new):
        self.cost = new

    def changeName(self, new):
        self.name = new

    def __str__(self):
        return self.name

class Category(common):
    def getCatData(self):
        return [self.pk, self.name]

    def changeName(self, new):
        self.name = new

    def __str__(self):
        return self.name


class PurchasedFood(models.Model):
    food = models.ForeignKey('Food', on_delete=models.PROTECT)
    purchase = models.ForeignKey('Purchase', on_delete=models.PROTECT)

    def getPurchFoodData(self):
        data = [self.pk, self.Food, self.purchase]
        return data

    def __str__(self):
        return self.pk


class Purchase(models.Model):
    customer_id = models.IntegerField()
    time_create = models.DateTimeField(auto_now_add=True)

    def getPurchase(self):
        data = [self.pk, self.customer_id, self.time_create]
        return data


