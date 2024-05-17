import dramatiq
from .models import Product

@dramatiq.actor
def update_product_stock(product_id, quantity):
    try:
        product = Product.objects.get(id=product_id)
        product.stock = ('stock') - quantity
        product.save()
    except Product.DoesNotExist:
        pass