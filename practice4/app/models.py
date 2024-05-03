from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Reseller(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class ModelManager(models.Model):
    def get_models_by_brand(self, brand):
        return self.filter(brand=brand)

    def get_models_by_reseller(self, reseller):
        return self.filter(reseller=reseller)


class ShowroomManager(models.Manager):
    def get_showrooms_by_reseller(self, reseller):
        return self.filter(reseller=reseller)

    def get_showrooms_by_model(self, model):
        return self.filter(model=model)


class Model(models.Model):
    name = models.CharField(max_length=20)
    horse_powers = models.IntegerField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    reseller = models.ForeignKey(Reseller, on_delete=models.CASCADE)
    objects = ModelManager()

    def __str__(self):
        return self.name


class Showroom(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    reseller = models.ForeignKey(Reseller, on_delete=models.CASCADE)
    objects = ShowroomManager()

    def __str__(self):
        return self.name
