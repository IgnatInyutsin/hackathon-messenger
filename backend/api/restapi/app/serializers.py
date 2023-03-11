from rest_framework import serializers
from .models import ClothItem, WeatherRecord


class ClothItemPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothItem
        fields = ["name", "temperature_min", "temperature_max", "type"]


class WeatherRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherRecord
        fields = '__all__'

class EmptySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherRecord
        fields = []