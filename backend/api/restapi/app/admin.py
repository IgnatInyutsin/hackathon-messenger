from django.contrib import admin
from .models import WeatherRecord, ClothItem


@admin.register(WeatherRecord)
class WeatherRecordAdmin(admin.ModelAdmin):
    list_display = ("__str__", "pressure", "wind_speed", "humidity")


@admin.register(ClothItem)
class ClothItemAdmin(admin.ModelAdmin):
    list_display = ("name", "type", )
