from django.test import TestCase
from django.contrib.auth.models import User
from restapi.app.models import Chat
from restapi.app.views import UserSearchViewSet, ChatViewSet

# Вспомогательный класс
class Request:
    query_params = dict()
    user = None

class ChatViewSetTestCase(TestCase):
    def setUp(self):
        # Создаем чаты
        self.chats = [Chat(name="test",type="pm"),
                Chat(name="test2", type="pm"),
                Chat(name="test3", type="gm")]

        # Создаем пользователя
        self.request = Request()
        self.request.user = User(id=1,
                                 username="test",
                                 password="test")
        self.request.user.save()


        # Сохраняем в бд
        for chat in self.chats:
            chat.save()
            chat.members.add(self.request.user)
            chat.save()

        # пустой чат
        Chat(name="test4", type="gm").save()


    def test_get_queryset_list(self):
        self.action = "list"
        self.assertEqual(len(ChatViewSet.get_queryset(self)), len(self.chats))