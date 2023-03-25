from django.test import TestCase
from django.contrib.auth.models import User
from restapi.app.models import Chat
from restapi.app.views import UserSearchViewSet, ChatViewSet

# Вспомогательный класс
class Request:
    query_params = dict()
    user = None

class UserSearchViewSetTestCase(TestCase):
    def setUp(self):
        # Создаем пользователей
        users = [User(username="tol", password="test"),
                 User(username="tolya", password="test"),
                 User(username="TOLya", password="test"),
                 User(username="toklya", password="test")]

        for user in users:
            user.save()

        # создаем queryset
        self.queryset = User.objects.all()

    def test_get_queryset(self):
        #тесты
        self.request = Request()
        self.request.query_params["username"] = "tol"
        self.assertEqual(len(UserSearchViewSet.get_queryset(self)), 3)

        self.request.query_params["username"] = "TOL"
        self.assertEqual(len(UserSearchViewSet.get_queryset(self)), 3)

        self.request.query_params["username"] = ""
        self.assertEqual(len(UserSearchViewSet.get_queryset(self)), 4)

        self.request.query_params["username"] = "test"
        self.assertEqual(len(UserSearchViewSet.get_queryset(self)), 0)

        self.request.query_params["username"] = "tokl"
        self.assertEqual(len(UserSearchViewSet.get_queryset(self)), 1)

        self.request.query_params["username"] = "TOLya"
        self.assertEqual(len(UserSearchViewSet.get_queryset(self)), 2)

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