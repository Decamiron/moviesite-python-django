# Generated by Django 3.2.8 on 2022-05-27 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Страна')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название серии фильмов')),
            ],
            options={
                'verbose_name': 'Серия фильмов',
                'verbose_name_plural': 'Серии фильмов',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='URL')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster_url', models.URLField(default='https://i.pinimg.com/originals/64/05/6b/64056b93adce628786363af7c03970f6.jpg', verbose_name='Картинка в интернете')),
                ('year', models.PositiveSmallIntegerField(default=2000, verbose_name='Дата выхода')),
                ('premiere', models.DateTimeField(verbose_name='Дата премьеры')),
                ('country', models.ManyToManyField(to='main.Country', verbose_name='страны')),
                ('genre', models.ManyToManyField(to='main.Genre', verbose_name='жанры')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.series', verbose_name='Серия фильмов')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'ordering': ['title'],
            },
        ),
    ]
