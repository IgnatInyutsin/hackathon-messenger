from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from restapi.app.models import Chat
from rest_framework import status
from rest_framework.request import Request
from restapi.app.views import UserSearchViewSet
from django.urls import reverse

class ChatViewSetTestCase(APITestCase):
    url = reverse("chat-list")
    url_detail_true = reverse("chat-detail", kwargs={"pk":1})
    url_detail_false = reverse("chat-detail", kwargs={"pk": 2})
    url_detail_404 = reverse("chat-detail", kwargs={"pk": 9999})
    user = User(id=1, username="test", password="test")

    def setUp(self):
        # сохраняем пользователя
        self.user.save()
        # принудительная аутенфикация пользователя во всех запросах
        self.client.force_authenticate(user=self.user)

    def test_list(self):
        # Создаем чаты c пользователем
        for i in range(5):
            chat = Chat(name="test", type="pm")
            chat.save()
            chat.members.add(self.user)
            chat.save()

        # Создаем чаты без пользователя
        for i in range(7):
            chat = Chat(name="test", type="pm")
            chat.save()

        # Делаем запрос
        response = self.client.get(self.url)
        # Проверяем
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data.get("results")), 5)

    def test_retrieve(self):
        # Создаем чат, в котором есть пользователь
        chat = Chat(id=1, name="test", type="pm")
        chat.save()
        chat.members.add(self.user)
        chat.save()

        # Создаем чат без пользователя
        Chat(id=2, name="test", type="pm").save()

        # делаем запросы
        response_true = self.client.get(self.url_detail_true)
        response_false = self.client.get(self.url_detail_false)
        response_404 = self.client.get(self.url_detail_404)
        # тестируем
        self.assertEqual(response_true.status_code, 200)
        self.assertEqual(response_false.status_code, 403)
        self.assertEqual(response_404.status_code, 403)

    def test_create(self):
        # делаем запрос на создание
        response = self.client.post(self.url, {"name": "test", "type": "pm", "members": [{"id": 1}]}, format="json")
        # тесты
        print(response.data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(Chat.objects.filter(members__in=[self.user])), 1)