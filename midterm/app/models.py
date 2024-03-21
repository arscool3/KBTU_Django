from django.db import models


class HotelQueryset(models.QuerySet):
    def get_queryset(self):
        return super().order_by('-stars')

    def filter_by_name(self, hotel_name):
        if hotel_name:
            return self.filter(name__iexact=hotel_name.capitalize())
        return self


class Hotel(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    stars = models.IntegerField(default=0)
    objects = HotelQueryset.as_manager()

    def __str__(self):
        return f"{self.name}:{self.stars} star"


class RoomQueryset(models.QuerySet):

    def get_rooms_by_hotel_name(self, hotel_name: str):
        return self.filter(hotel__name=hotel_name)

    def get_rooms_by_type(self, type_name: str):
        return self.filter(type=type_name)

    def available(self):
        return self.filter(available=True)

    def not_available(self):
        return self.filter(available=False)


class Room(models.Model):
    TYPES = [
        ('double', 'Double'),
        ('king', 'King'),
        ('two_double', 'Two Double'),
        ('suite', 'Suite')
    ]

    room_no = models.IntegerField(unique=True)
    type = models.CharField(max_length=20, choices=TYPES)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    objects = RoomQueryset.as_manager()

    def __str__(self):
        return f"Room: {self.room_no} - ${self.price}"


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation for {self.customer} - Room No {self.room.room_no}"
