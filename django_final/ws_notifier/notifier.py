from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class WebsocketNotifier:

    def __init__(self):
        self._channel = get_channel_layer()

    def notify(self, payload: dict, group: str = "recipients"):
        async_to_sync(self._channel.group_send)(
            group, payload
        )
