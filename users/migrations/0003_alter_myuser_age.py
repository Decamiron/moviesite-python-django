# Generated by Django 3.2.7 on 2021-10-06 18:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211006_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, default=18, validators=[django.core.validators.MinValueValidator(8), django.core.validators.MaxValueValidator(100)], verbose_name='Возраст'),
        ),
    ]
