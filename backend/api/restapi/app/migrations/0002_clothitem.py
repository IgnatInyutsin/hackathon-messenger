# Generated by Django 3.2.16 on 2023-02-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClothItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=200, verbose_name='Название одежды')),
                ('image_url', models.URLField(blank=True, null=True, verbose_name='Ссылка на изображение')),
                ('temperature_min', models.IntegerField(verbose_name='Минимальная температура')),
                ('type', models.IntegerField(choices=[(1, 'Верхняя одежда'), (2, 'Головной убор'), (3, 'Чулочно-носочные изделия'), (4, 'Перчаточные изделия'), (5, 'Шарфы/платки'), (6, 'Обувь')], verbose_name='Тип одежды')),
            ],
        ),
    ]
