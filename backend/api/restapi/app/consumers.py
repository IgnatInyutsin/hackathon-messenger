import json
from channels.generic.websocket import AsyncWebsocketConsumer
from restapi.app.models import Chat, Message
from asgiref.sync import sync_to_async
class ChatConsumer(AsyncWebsocketConsumer):
    user = None
    chat_id = None
    chat = None

    async def connect(self):
        # получаем данные о пользователе
        self.user = self.scope['user']

        # получаем данные о чате. Проверяем доступ
        self.chat_id = self.scope["url_route"]["kwargs"]["chat_id"]
        self.chat = await sync_to_async(Chat.objects.filter)(id=self.chat_id, members__in=[self.user])
        chat_len = await sync_to_async(len)(self.chat)

        if chat_len == 0:
            self.close()
            return
        else:
            self.chat = self.chat[0]

        # добавляем в нужный слой
        await self.channel_layer.group_add(self.chat_id, self.channel_name)

        # подтверждаем рукопожатие
        await self.accept()
        print("OK")

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.chat_id, self.channel_name)

    async def receive(self, text_data):
        # получаем данные о сообщении
        try:
            text_data_json = json.loads(text_data)
        except json.decoder.JSONDecodeError:
            await self.channel_layer.group_send(
                self.chat_id, {"type": "chat_message_error", "data": "Uncorrect data format"}
            )
            return
        forward_message = None

        # получаем отвечаемое сообщение
        if "forward_message_id" in text_data_json:
            forward_message = await sync_to_async(Message.objects.get)(id=text_data_json["forward_message"])
            if forward_message.chat.id != self.chat_id:
                # отправляем сообщение об ошибке
                await self.channel_layer.group_send(
                    self.chat_id, {"type": "chat_message_error", "data": "Uncorrect forward message"}
                )
                return
            else:
                text_data_json["forward_message_author_name"] = forward_message.author.name
                text_data_json["forward_message_author_id"] = forward_message.author.id
                text_data_json["forward_message_text"] = forward_message.text

        if not "text" in text_data_json:
            await self.channel_layer.group_send(
                self.chat_id, {"type": "chat_message_error", "data": "Empty text"}
            )
            return

        text_data_json["author_name"] = self.user.username
        text_data_json["author_id"] = self.user.id
        text_data_json["chat_id"] = self.chat.id
        text_data_json["chat_name"] = self.chat.name

        # сохраняем в базу данных
        message_obj = Message(
            text=text_data_json["text"],
            forward_message=forward_message,
            author=self.user,
            chat=self.chat
        )
        await sync_to_async(message_obj.save)()

        # отправляем сообщение всем
        await self.channel_layer.group_send(
            self.chat_id, {"type": "chat_message", "data": text_data_json}
        )

    # Обработчик сообщений от сервера этого типа
    async def chat_message(self, event):
        # Отправка всем по веб сокету
        await self.send(text_data=json.dumps(event["data"]))

    async def chat_message_error(self, event):
        await self.send(text_data=json.dumps(event["data"]))
