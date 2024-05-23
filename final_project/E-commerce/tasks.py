import dramatiq

@dramatiq.actor
def send_order_confirmation(user_id, order_id):
    print(f"Sending order confirmation to user {user_id} for order {order_id}")




