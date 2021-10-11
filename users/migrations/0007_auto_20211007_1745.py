# Generated by Django 3.2.7 on 2021-10-07 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20211007_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmusersinfo',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='Публичный список фильмов'),
        ),
    ]