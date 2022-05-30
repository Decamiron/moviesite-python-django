from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Avg
from django.urls import reverse


class Genre(models.Model):
    title = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    slug = models.SlugField("URL", max_length=100, unique=True, db_index=True)

    def get_films(self):
        return self.films.all()

    def clean(self):
        if not self.slug or not self.title:
            raise ValidationError("Invalid data")

        if self.slug in self._meta.model.objects.all().values_list('slug', flat=True):
            raise ValidationError("Этот слаг уже существует")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ['title']


class Country(models.Model):
    title = models.CharField("Страна", max_length=100)
    slug = models.SlugField("URL", max_length=100, unique=True, db_index=True)

    def get_films(self):
        return self.films.all()

    def clean(self):
        if not self.slug or not self.title:
            raise ValidationError("Invalid data")

        if self.slug in self._meta.model.objects.all().values_list('slug', flat=True):
            raise ValidationError("Этот слаг уже существует")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"
        ordering = ['title']


class Series(models.Model):
    title = models.CharField("Название серии фильмов", max_length=100)
    slug = models.SlugField("URL", max_length=100, unique=True, db_index=True)

    def get_films(self):
        return self.films.all()

    def clean(self):
        if not self.slug or not self.title:
            raise ValidationError("Invalid data")

        if self.slug in self._meta.model.objects.all().values_list('slug', flat=True):
            raise ValidationError("Этот слаг уже существует")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Серия фильмов"
        verbose_name_plural = "Серии фильмов"
        ordering = ['title']


class Film(models.Model):
    title = models.CharField("Название", max_length=100)
    slug = models.SlugField("URL", max_length=100, unique=True, db_index=True)
    description = models.TextField("Описание")
    poster_url = models.URLField("Картинка в интернете", default=settings.DEFAULT_IMAGE)
    year = models.PositiveSmallIntegerField("Дата выхода", default=2000)
    country = models.ManyToManyField("Country", verbose_name='страны', related_name='films')
    genre = models.ManyToManyField('Genre', verbose_name='жанры', related_name='films')
    premiere = models.DateTimeField("Дата премьеры")
    series = models.ForeignKey('Series', on_delete=models.PROTECT, verbose_name='Серия фильмов', related_name='films')

    def get_reviews(self):
        return self.filmusersinfo_set.filter(rating__isnull=False)

    def get_countries(self):
        return self.country.all()

    def get_genres(self):
        return self.genre.all()

    def get_film_rating(self):
        return self.filmusersinfo_set.filter(film_id=self.pk).aggregate(res=Avg('rating'))

    def get_title(self):
        return str(self.title)

    def clean(self):
        if not (self.slug and self.title and self.description and self.poster_url and self.year and self.country \
                and self.genre and self.premiere and self.series):
            raise ValidationError("Invalid data")

        if self.slug in self._meta.model.objects.all().values_list('slug', flat=True):
            raise ValidationError("Этот слаг уже существует")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"
        ordering = ['title']

    def get_absolute_url(self):
        return reverse("main:movie_detail", kwargs={"movie_slug": self.slug})
