from django.db import models
from django.conf import settings

# Query Sets

class ProductQuerySets(models.QuerySet):
    def get_all_products(self):
        return self.all()

    def get_cat_pr(self, cat_id):
        return self.filter(cat=cat_id)


class CategoryQuerySets(models.QuerySet):
    def get_all_categories(self):
        return self.all()

class BusketItemsQuerySet(models.QuerySet):
    def get_UserBusket(self, User_id):
        return self.filter(user=User_id)

    def get_purchased(self):
        return self.all().exclude(purch=None)

    def get_not_purchased(self):
        return self.filter(purch=None)

    def addItem(self, p, a, u):
        p = Product.objects.get(pk=p)

        b = self.create(product=p, amount=a, user=u)
        b.save()


class PurchQuerySets(models.QuerySet):
    def makePurch(self, u, a, c):
        p = self.create(user=u, adress=a, cost=c)
        p.save()

        return p

class UserInfoQuerySets(models.QuerySet):
    def just_registrated(self, u):
        ui = self.create(user=u)
        ui.save()

class Product(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    desc = models.TextField(blank=True)
    cost = models.IntegerField()
    amount = models.IntegerField()
    available = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)
    objects = ProductQuerySets.as_manager()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    objects = CategoryQuerySets.as_manager()

    def __str__(self):
        return self.name


class UserInfo(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    desc = models.TextField(blank=True)
    default_address = models.OneToOneField('Adress', on_delete=models.SET_NULL, blank=True, null=True)
    objects = UserInfoQuerySets.as_manager()

    def __str__(self):
        return f'{self.user.username} Info'



class Adress(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house = models.CharField(max_length=255)
    index = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user.username} adress id:{self.id}'


class BusketItems(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    amount = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    purchased = models.BooleanField(default=False)
    purch = models.ForeignKey('Purchase', on_delete=models.CASCADE, blank=True, null=True)
    objects = BusketItemsQuerySet.as_manager()

    def __str__(self):
        return f'{self.user.username} item id: {self.id}'

class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    adress = models.ForeignKey('Adress', on_delete=models.PROTECT)
    cost = models.IntegerField()
    objects = PurchQuerySets.as_manager()

    def __str__(self):
        return f'{self.user.username} date: {self.date}'