# Generated by Django 3.2.8 on 2021-10-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_filmusersinfo_series'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmusersinfo',
            name='comment',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='filmusersinfo',
            name='raiting',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, verbose_name='Рейтинг'),
        ),
    ]
