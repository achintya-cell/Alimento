# Generated by Django 3.1.1 on 2021-01-03 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0002_auto_20210103_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.CharField(choices=[('starter', 'Starter'), ('main food', 'Mainfood'), ('specials', 'Specials'), ('dessert', 'Dessert'), ('drinks', 'Drinks')], max_length=100),
        ),
    ]
