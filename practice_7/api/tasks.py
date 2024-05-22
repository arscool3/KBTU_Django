import dramatiq
from django.core.mail import send_mail
from .models import Order

@dramatiq.actor
def order_confirmation(order_id):
    try:
        order = Order.objects.get(id=order_id)
        subject = 'Order Confirmation'
        message = f'Hi {order.user.username},\n\nYour order has been placed successfully.\n\nOrder ID: {order.id}\nTotal Price: ${order.total_price}\n\nThank you for shopping with us!'
        sender_email = 'gzagipar@gmail.com'
        recipient_email = order.user.email
        send_mail(subject, message, sender_email, [recipient_email])
    except Order.DoesNotExist:
        print(f"Order with ID {order_id} does not exist.")
