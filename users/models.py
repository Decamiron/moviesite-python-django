from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
import datetime as date


class MyUser(AbstractUser):
    photo = models.ImageField('Фотография', upload_to='users_photo', blank=True, default='users/unknow.png')
    birth_date = models.DateField('День Рождения', default='2002-09-20', blank=True, validators=[MinValueValidator(limit_value=date.date(1900, 1, 1)), MaxValueValidator(limit_value=date.date.today)])
    age = models.PositiveSmallIntegerField("Возраст", default=18, blank=True, validators=[MinValueValidator(8), MaxValueValidator(100)])
    about_user = models.TextField("О себе", blank=True, max_length=500)
    is_published = models.BooleanField('Публичный список фильмов', default=True)
    REQUIRED_FIELDS = ['email']

    def get_username(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"id": self.pk})

    class Meta():
        verbose_name = "Юзер"
        verbose_name_plural = "Юзеры"


class FilmUsersInfo(models.Model):
    none_list = ''
    planned = 'Planned'
    viewed = 'Viewed'
    abandoned = 'Abandoned'

    FILMLIST = (
        (planned, 'Запланировано'),
        (viewed, 'Прсомотрено'),
        (abandoned, 'Брошено'),
        (none_list, 'Не в списке'),
    )

    RATING = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    rating = models.PositiveSmallIntegerField('Рейтинг', choices=RATING, blank=True, null=True)
    comment = models.TextField('Комментарий', max_length=1000, blank=True, null=True)
    filmlist = models.CharField('Список', choices=FILMLIST, blank=True, max_length=9, default=None)
    user = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    film = models.ForeignKey('main.Film', on_delete=models.CASCADE)

    def __str__(self):
        return f'Review: _{self.user.get_username()}_ to {self.film.get_title()}'

    class Meta():
        verbose_name = "Информация о фильме"
        verbose_name_plural = "Информация о фильмах"

