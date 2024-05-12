from channels.generic.websocket import AsyncJsonWebsocketConsumer

from users.models import User


class NotificationConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        if self.scope["user"].is_authenticated:
            await self.channel_layer.group_add(
                f'{self.scope["user"].id}',
                self.channel_name
            )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            f'{self.scope["user"].id}',
            self.channel_name
        )

    async def send_notification(self, event):
        await self.send_json(event)

    async def send_notification_to_user(self, event):
        try:
            if event["user_id"] == str(self.scope["user"].id):
                await self.send_json(event)
        except User.DoesNotExist as e:
            raise e
