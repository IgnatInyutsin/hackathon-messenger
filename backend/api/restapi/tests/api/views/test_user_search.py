from rest_framework.test import APIRequestFactory, APITestCase
from rest_framework.test import force_authenticate
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.request import Request
from restapi.app.views import UserSearchViewSet
from django.urls import reverse

class UserSearchViewSetTestCase(APITestCase):
    url = reverse("user-search-list")
    # Данные типа - запрос/длина
    response_validators_set = (
        ("tol", 3),
        ("TOL", 3),
        ("", 4),
        ("test", 0),
        ("tokl", 1),
        ("TOLya", 2)
    )

    def setUp(self):
        # Создаем пользователей
        users = [
            User(username="tol", password="test"),
            User(username="tolya", password="test"),
            User(username="TOLya", password="test"),
            User(username="toklya", password="test")
        ]

        for user in users:
            user.save()

    # тест на 200_OK код
    def test_response_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # тест на выполнение своего функционала
    def test_functional(self):
        # тестируем по датасету
        for i in range(len(self.response_validators_set)):
            response = self.client.get(self.url, {"username": self.response_validators_set[i][0]})
            self.assertEqual(len(response.data.get("results")), self.response_validators_set[i][1])