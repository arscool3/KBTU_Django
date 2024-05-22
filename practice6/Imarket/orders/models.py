import datetime

from django.db import models
from users.models import User
from shop.models import WarehouseItem
from users.choices import Role


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, limit_choices_to={'user_type': Role.CUSTOMER})
    completed = models.BooleanField(default=False)
    delivery_date = models.DateTimeField(verbose_name='Delivery Date', null=True)
    delivery_address = models.CharField(max_length=255, verbose_name='Address of deliver', default="address")
    delivery_price = models.FloatField(default=0)

    def __str__(self):
        return f'order_id: {self.pk} || ' \
               f'{self.completed}, {self.delivery_date}, {self.delivery_address}, {self.delivery_price} || ' \
               f'----- user: {self.user}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    warehouse_item = models.ForeignKey(WarehouseItem, on_delete=models.PROTECT, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'order_item_id: {self.pk} ' \
               f'--- wh: {self.warehouse_item.product.name} ' \
               f'--- order_id: {self.order.id}' \
               f'--- user_id: {self.order.user_id}'
