from datetime import timezone
from django.db import models

class Entity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(Entity):
    name = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class CustomerQuerySet(models.QuerySet):
    def with_phone_number(self):
        return self.exclude(phone_number='')

    def without_email(self):
        return self.filter(email='')

    def created_before_date(self, date):
        return self.filter(created_at__lt=date)

    def created_after_date(self, date):
        return self.filter(created_at__gt=date)

    def name_starts_with(self, letter):
        return self.filter(name__istartswith=letter)

    def name_contains_word(self, word):
        return self.filter(name__icontains=word)

class OrderQuerySet(models.QuerySet):
    def with_delivery(self):
        return self.filter(is_delivery=True)

    def without_delivery(self):
        return self.filter(is_delivery=False)

    def placed_in_month(self, month):
        return self.filter(created_at__month=month)

    def placed_in_year(self, year):
        return self.filter(created_at__year=year)

    def total_price_less_than(self, amount):
        return self.filter(total_price__lt=amount)

    def total_price_between(self, min_amount, max_amount):
        return self.filter(total_price__range=(min_amount, max_amount))

class Customer(User):
    email = models.EmailField(unique=True)
    # Assuming you want a ManyToMany relationship between Customer and Order
    orders = models.ManyToManyField('Order', related_name='customers')

    objects = CustomerQuerySet.as_manager()

    def __str__(self):
        return self.name

class MenuItem(Entity):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Order(Entity):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = OrderQuerySet.as_manager()

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"

class OrderItem(Entity):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.menu_item.name}"

class Delivery(Entity):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    delivery_address = models.TextField()

    def __str__(self):
        return f"Delivery for Order {self.order.id}"
