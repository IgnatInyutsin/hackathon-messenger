import requests
from restapi.app.models import WeatherRecord
from datetime import datetime
from django.db import transaction

# используем транзакции в функции
@transaction.atomic
def cash_forecast(city):
    response = requests.get("https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&limit=7&APPID=5d5631a0332bcd2f009a28a913627452"
                            .format(city=city))
    response_data = response.json().get("list", [])
    for i in range(len(response_data)):
        # преобразуем текст в объект datetime
        date_i = datetime.strptime(response_data[i]["dt_txt"], '%Y-%m-%d %H:%M:%S')
        if len(WeatherRecord.objects.filter(city=city.upper(), day=date_i)) == 0:
            # если не cуществует записи - создаем
            obj = WeatherRecord(city=city.upper(),
                                day=date_i,
                                pressure=response_data[i]["main"]["pressure"],
                                humidity=response_data[i]["main"]["humidity"],
                                temperature=(response_data[i]["main"]["temp_min"] + response_data[i]["main"]["temp_max"])//2,
                                wind_speed=response_data[i]["wind"]["speed"])
            obj.clean()
            obj.save()