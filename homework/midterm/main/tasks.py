# tasks.py

import dramatiq
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import *

@dramatiq.actor
def update_order_details(order_id):
    order = Order.objects.get(id=order_id)
    basket_items = In_Basket.objects.filter(basket__user=order.user)
    order_items = {}
    for item in basket_items:
        order_items[item.product_id] = order_items.get(item.product_id, 0) + item.quantity
    
    In_Order.objects.filter(order=order).delete()
    for product_id, quantity in order_items.items():
        In_Order.objects.create(order=order, product_id=product_id, quantity=quantity)

@receiver([post_save, post_delete], sender=In_Basket)
def handle_basket_change(sender, instance, **kwargs):
    update_order_details.send(instance.basket.order.id)
