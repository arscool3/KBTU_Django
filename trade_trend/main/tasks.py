from celery import shared_task
from .models import Order, Notification

@shared_task
def notify_user_of_order(order_id):
    order = Order.objects.get(id=order_id)
    notification_text = f'Your order #{order.id} status has been updated to {order.status}'
    Notification.objects.create(user=order.user, notification_text=notification_text)