import datetime

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

from users.utils import birthday_validators, age_validators


class MyUser(AbstractUser):
    photo = models.ImageField('Фотография', upload_to='users_photo', null=True, default='users/unknow.png')
    birth_date = models.DateField('День Рождения', null=True, validators=birthday_validators())
    age = models.PositiveSmallIntegerField("Возраст", null=True, validators=age_validators())
    about_user = models.TextField("О себе", blank=True, max_length=500)
    is_published = models.BooleanField('Публичный список фильмов', default=True)
    REQUIRED_FIELDS = ['email']

    def clean(self):
        super(MyUser, self).clean()
        if not self.email or not self.username:
            raise ValidationError("no email or username")

    def save(self, *args, **kwargs):
        if self.birth_date:
            self.age = datetime.datetime.now().year - self.birth_date.year

        super(MyUser, self).save(*args, **kwargs)

    def get_viewed_films(self, filmlist):
        user_reviews = self.filmusersinfo_set.filter(filmlist=filmlist)
        if user_reviews:
            return [ur.film for ur in user_reviews]

    def has_subscription(self):
        return self.subscription.exists()

    def get_username(self):
        return str(self.username)

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"id": self.pk})

    class Meta:
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
    comment = models.TextField('Комментарий', max_length=1000, blank=True)
    filmlist = models.CharField('Список', choices=FILMLIST, blank=True, max_length=9, default=None)
    user = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    film = models.ForeignKey('main.Film', on_delete=models.CASCADE)

    def __str__(self):
        return f'Review: _{self.user.get_username()}_ to {self.film.get_title()}'

    class Meta:
        verbose_name = "Информация о фильме"
        verbose_name_plural = "Информация о фильмах"

