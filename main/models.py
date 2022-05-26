from django.conf import settings
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    slug = models.SlugField("URL", max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ['name']


class Country(models.Model):
    name = models.CharField("Страна", max_length=100)
    slug = models.SlugField("URL", max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
        ordering = ['name']


class Series(models.Model):
    name = models.CharField("Название серии фильмов", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Серия фильмов"
        verbose_name_plural = "Серии фильмов"
        ordering = ['name']


class Film(models.Model):
    title = models.CharField("Название", max_length=100)
    slug = models.SlugField("URL", max_length=100, unique=True, db_index=True)
    description = models.TextField("Описание")
    poster_url = models.URLField("Картинка в интернете", default=settings.DEFAULT_IMAGE)
    year = models.PositiveSmallIntegerField("Дата выхода", default=2000)
    country = models.ManyToManyField("Country", verbose_name='страны')
    genre = models.ManyToManyField('Genre', verbose_name='жанры')
    premiere = models.DateTimeField("Дата премьеры")
    series = models.ForeignKey('Series', on_delete=models.PROTECT, verbose_name='Серия фильмов')

    def get_title(self):
        return str(self.title)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ['title']

    def get_absolute_url(self):
        return reverse("main:movie_detail", kwargs={"movie_slug": self.slug})
