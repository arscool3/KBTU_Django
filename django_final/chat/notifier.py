from ws_notifier.notifier import WebsocketNotifier


class MessageNotifier:

    def __init__(self):
        self.ws = WebsocketNotifier()

    def notify(self, user_id, message):
        self.ws.notify(
            {
                "type": "send_notification_to_user",
                "event": "chat_message",
                "user_id": str(user_id),
                "message": message,
            },
            group=str(user_id),
        )