# Generated by Django 3.1.1 on 2021-01-03 15:37

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0007_auto_20210103_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]