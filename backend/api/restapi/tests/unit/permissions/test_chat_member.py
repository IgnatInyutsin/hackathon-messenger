from django.test import TestCase
from restapi.app.permissions import *
from restapi.app.models import Chat
from django.contrib.auth.models import User

# классы-затычки для тестирования
class ResolverMatch:
    kwargs = dict()
class Request:
    resolver_match = ResolverMatch()
    user = None



class PermissionTestCase(TestCase):
    def setUp(self):
        pass

    def test_permission_success(self):
        # создаем классы для тестирования
        request = Request()
        request.resolver_match.kwargs["pk"] = 1

        # Создаем пользователя
        request.user = User(id=1,
                            username="test",
                            password="test",
                            email="test@test.com")
        request.user.save()

        # Создаем чат
        chat = Chat(id=1,
                    name="test",
                    type="pm")
        chat.save()
        chat.members.add(request.user)
        chat.save()

        self.assertEqual(ChatMemberPermission.has_permission(None, request, None), True)

    def test_permission_denied_without_user(self):
        # создаем классы для тестирования
        request = Request()
        request.resolver_match.kwargs["pk"] = 1

        # Создаем пользователя
        request.user = User(id=1,
                            username="test",
                            password="test",
                            email="test@test.com")
        request.user.save()

        # Создаем чат
        chat = Chat(id=1,
                    name="test",
                    type="pm")
        chat.save()

        self.assertEqual(ChatMemberPermission.has_permission(None, request, None), False)

    def test_permission_denied_with_fake_id(self):
        # создаем классы для тестирования
        request = Request()
        request.resolver_match.kwargs["pk"] = 999

        # Создаем пользователя
        request.user = User(id=1,
                            username="test",
                            password="test",
                            email="test@test.com")
        request.user.save()

        # Создаем чат
        chat = Chat(id=1,
                    name="test",
                    type="pm")
        chat.save()
        chat.members.add(request.user)
        chat.save()

        self.assertEqual(ChatMemberPermission.has_permission(None, request, None), False)