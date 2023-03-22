import json
from channels.generic.websocket import AsyncWebsocketConsumer
from restapi.app.models import Chat, Message
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.chat_group_name = "chat_%s" % self.chat_id
        self.user = self.scope["user"]

        if not user.is_authenticated():
            return False
        if not user in Chat.objects.get(id=chat_id).members:
            return False

        # Join room group
        await self.channel_layer.group_add(self.chat_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.chat_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        message_obj = Message(
            text=message["text"],
            forward_message=Message.objects.get(id=message["forward_message"])
                if len(Message.objects.all(id=message["forward_message"])) > 0 else None,
            author=self.user,
            chat=Chat.objects.get(id=self.chat_id)
        )
        message_obj.save()

        # Send message to room group
        await self.channel_layer.group_send(
            self.chat_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))