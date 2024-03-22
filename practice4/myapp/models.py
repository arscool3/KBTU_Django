from django.db import models

# Define custom managers
class CustomManager1(models.Manager):
    def method1(self):
        # Method logic
        pass

    def method2(self):
        # Method logic
        pass

class CustomManager2(models.Manager):
    def method1(self):
        # Method logic
        pass

    def method2(self):
        # Method logic
        pass

# Define models
class Model1(models.Model):
    name = models.CharField(max_length=100)
    objects = CustomManager1()  # Assigning custom manager

class Model2(models.Model):
    model1 = models.ForeignKey(Model1, on_delete=models.CASCADE)
    description = models.TextField()
    objects = CustomManager2()  # Assigning custom manager

class Model3(models.Model):
    model2 = models.ManyToManyField(Model2)
    created_at = models.DateTimeField(auto_now_add=True)

class Model4(models.Model):
    model3 = models.OneToOneField(Model3, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
