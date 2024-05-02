import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "group_main"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_layer
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        time = text_data_json["time"]
        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": message,
                "username": username,
                "time": time
            })

    async def sendMessage(self, event):
        message = event["message"]
        username = event["username"]
        time = event["time"]

        await self.send(text_data=json.dumps(
            {
                "message": message,
                "username": username,
                "time": time
            }
        ))

class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        username = text_data_json["username"]
        time = text_data_json["time"]
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'time': time
            }
        )

    async def chat_message(self, event):
        message = event['message']
        username = event["username"]
        time = event["time"]
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
            'time': time
        }))


class ChatNotification(AsyncWebsocketConsumer):
    async def connect(self):
        self.roomGroupName = "group_not"
        await self.channel_layer.group_add(
            self.roomGroupName,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.roomGroupName,
            self.channel_layer
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        notification_from = text_data_json["notification_from"]
        message = text_data_json["message"]
        group = text_data_json["group"]
        print(notification_from)
        await self.channel_layer.group_send(
            self.roomGroupName, {
                "type": "sendMessage",
                "message": message,
                "notification_from":notification_from,
                "group": group
            })

    async def sendMessage(self, event):
        message = event["message"]
        notification_from = event["notification_from"]
        group = event["group"]
        await self.send(text_data=json.dumps(
            {
                "message": message,
                "notification_from": notification_from,
                "group": group
            }
        ))
