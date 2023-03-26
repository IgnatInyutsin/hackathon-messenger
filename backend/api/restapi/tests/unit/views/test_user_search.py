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