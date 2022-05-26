from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

from users.utils import get_date_validators, get_age_validators


class MyUser(AbstractUser):
    photo = models.ImageField('Фотография', upload_to='users_photo', null=True, default='users/unknow.png')
    birth_date = models.DateField('День Рождения', null=True, validators=get_date_validators())
    age = models.PositiveSmallIntegerField("Возраст", null=True, validators=get_age_validators())
    bio = models.TextField("О себе", blank=True, max_length=500)
    published_film_list = models.BooleanField('Публичный список фильмов', default=True)
    REQUIRED_FIELDS = ['email']

    def get_username(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"id": self.pk})

    class Meta:
        verbose_name = "Юзер"
        verbose_name_plural = "Юзеры"


class FilmUsersInfo(models.Model):
    FILMLIST = (
        ('Planned', 'Запланировано'),
        ('Viewed', 'Прсомотрено'),
        ('Abandoned', 'Брошено'),
        ('', 'Не в списке'),
    )

    RAITING = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    grade = models.PositiveSmallIntegerField('Рейтинг', choices=RAITING)
    comment = models.TextField('Комментарий', max_length=1000, blank=True)
    series = models.CharField('Список', choices=FILMLIST, default='', max_length=9)
    user = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    film = models.ForeignKey('main.Film', on_delete=models.CASCADE)

    def __str__(self):
        return f'Review: _{self.users_info.get_username()}_ to {self.film_info.get_title()}'

    class Meta:
        verbose_name = "Информация о фильме"
        verbose_name_plural = "Информация о фильмах"

