from django.core.exceptions import ValidationError
from django.db import models

from products.models import Product
from users.models import User
from users.choices import Role

def validate_rating(value):
    if 0 <= value <= 5:
        return value
    else:
        raise ValidationError("This field accepts rating between 0 and 5")


class Shop(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Shop')
    rating = models.FloatField(default=5, verbose_name='Rating', validators=[validate_rating, ])
    rate_cnt = models.IntegerField(null=True, default=1)
    address = models.CharField(max_length=255, verbose_name='Shop address', unique=True)

    seller = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='seller_shops',
        limit_choices_to={'user_type': Role.SELLER},)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'
        ordering = ('-rating', 'name')

    def __str__(self):
        return f'{self.name} - rating: ({self.rating})'

    def get_products(self):
        return self.product_set.all()


class WarehouseItem(models.Model):
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    class Meta:
        verbose_name = 'warehouse item'
        verbose_name_plural = 'warehouse items'

    def __str__(self):
        return f'whi_id: {self.pk}, product: {self.product.name}, shop: {self.shop.name}, ' \
               f'price: {self.price}, quantity_in_wh: {self.quantity}'
