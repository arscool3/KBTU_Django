from celery import shared_task
from .models import Order

@shared_task
def notify_user_of_order(order_id):
    order = Order.objects.get(id=order_id)
    # logic to notify user
    return "User notified"