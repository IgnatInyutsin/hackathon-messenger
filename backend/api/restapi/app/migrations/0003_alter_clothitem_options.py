# Generated by Django 3.2.16 on 2023-02-26 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_clothitem'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clothitem',
            options={'verbose_name': 'Элемент одежды', 'verbose_name_plural': 'Элементы одежды'},
        ),
    ]
