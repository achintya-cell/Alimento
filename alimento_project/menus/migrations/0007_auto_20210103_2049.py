# Generated by Django 3.1.1 on 2021-01-03 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0006_auto_20210103_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='image',
            field=models.ImageField(upload_to='menu/'),
        ),
    ]
