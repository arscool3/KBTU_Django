from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class DriverLicense(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return f"Driver's License of {self.user.username}"

class Car(models.Model):
    user = models.ManyToManyField(User)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    license_plate = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.license_plate})"

class ParkingLot(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    total_spaces = models.IntegerField()

    def __str__(self):
        return self.name

class ParkingSpace(models.Model):
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    car = models.OneToOneField(Car, on_delete=models.SET_NULL, null=True, blank=True)
    space_number = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Space {self.space_number} at {self.parking_lot}"

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment for {self.user} at {self.parking_space} on {self.start_time}"
