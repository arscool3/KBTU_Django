from celery import shared_task
from .models import Product

@shared_task
def update_product_stock(product_id, quantity):
    try:
        product = Product.objects.get(id=product_id)
        product.stock = ('stock') - quantity
        product.save()
    except Product.DoesNotExist:
        pass