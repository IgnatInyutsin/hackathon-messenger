from rest_framework import viewsets, mixins, permissions
from restapi.app.serializers import *
from restapi.app.models import *
from rest_framework.serializers import ValidationError
from restapi.app.weatherapi import cash_forecast
from datetime import datetime
from rest_framework.authtoken.models import Token
from django.db import transaction
from rest_framework.response import Response
from rest_framework import status
from restapi.app.recommendation import *

class WeatherViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = WeatherRecord.objects.all()
    serializer_class = WeatherRecordSerializer
    permission_classes = (permissions.AllowAny,)

    def get_queryset(self):
        city = self.request.query_params.get("city", "")

        if city == "":
            return None

        cash_forecast(city)
        return WeatherRecord.objects.filter(day__gt=datetime.now(), city=city.upper())

class ClothViewSet(mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    queryset = ClothItem.objects.all()
    serializer_class = ClothItemPostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = ClothItemPostSerializer(data=request.data)
        if serializer.is_valid():
            # получаем зарегистрированного пользователя
            user = Token.objects.get(key=request.headers.get("Authorization")[6:]).user
            # рассчитываем тепловое сопротивление
            thermal_resistance_min = (0.0098518285*(33-request.data.get("temperature_max")) - 0.1425)/0.155
            thermal_resistance_max = (0.0098518285*(33-request.data.get("temperature_min")) - 0.1425)/0.155
            # сохраняем объект
            obj = ClothItem(user=user,
                            name=request.data.get("name"),
                            temperature_min=request.data.get("temperature_min"),
                            temperature_max=request.data.get("temperature_max"),
                            type=request.data.get("type"),
                            thermal_resistance_min=thermal_resistance_min,
                            thermal_resistance_max=thermal_resistance_max)
            obj.save()
            #возвращаем 200
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            # если не прошел сериализацию - возвращаем error
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class RecommendationViewSet(mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = WeatherRecord.objects.all()
    serializer_class = EmptySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        weather_id = self.request.query_params.get("weather_id", "")

        if weather_id == "":
            return Response({"status": "error", "data": ["weather_id is empty"]}, status=status.HTTP_400_BAD_REQUEST)
        if len(WeatherRecord.objects.filter(id=weather_id)) == 0:
            return Response({"status": "error", "data": ["weather_id is undefined"]}, status=status.HTTP_400_BAD_REQUEST)

        user = Token.objects.get(key=request.headers.get("Authorization")[6:]).user

        return Response(get_user_recomendations(user.id, WeatherRecord.objects.get(id=weather_id)), status=status.HTTP_201_CREATED)