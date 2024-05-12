from ws_notifier.notifier import WebsocketNotifier


class OrderStatusChangeNotifier:

    def __init__(self):
        self.ws = WebsocketNotifier()

    def notify(self, user_id, order_data):
        self.ws.notify(
            {
                "type": "send_notification_to_user",
                "event": "order_status_change",
                "user_id": str(user_id),
                "data": order_data,
            },
            group=str(user_id),
        )
