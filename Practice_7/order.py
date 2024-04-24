import random

orders = {
    "order1": {"status": "Processing", "shipping_tracking_number": "XYZ123"},
    "order2": {"status": "In Transit", "shipping_tracking_number": "ABC987"},
    "order3": {"status": "Delivered", "shipping_tracking_number": "LMN456"}
}


def fetch_order(order_id):
    return orders.get(order_id, None)


def update_order_status(order_id, status):
    if order_id in orders:
        orders[order_id]['status'] = status
        return True
    return False


def check_delivery_status(tracking_number):
    return random.choice(["Delivered", "In Transit", "Delayed"])