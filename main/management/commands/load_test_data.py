import datetime

from django.core.management.base import BaseCommand
from users.models import MyUser, FilmUsersInfo
from subscriptions.models import SubscriptionType, Subscription
from main.models import Film, Genre, Country, Series


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        user, _ = MyUser.objects.get_or_create(username="TestUser", email="test@gmail.com", age=19)

        series, _ = Series.objects.get_or_create(title="Test Series", slug="test_series")
        genre, _ = Genre.objects.get_or_create(title="Test Genre", slug="test_genre")
        country, _ = Country.objects.get_or_create(title="Test Country", slug="test_country")

        film, _ = Film.objects.get_or_create(
            title="test title",
            slug="test_title",
            description="test,description",
            year=1998,
            series=series,
            premiere=datetime.datetime(2022, 8, 20, 20),
        )
        film.country.add(country)
        film.genre.add(genre)
        film.save()

        FilmUsersInfo.objects.get_or_create(
            rating=4,
            comment="Test comment",
            filmlist=0,
            user=user,
            film=film
        )

        subscription_type, _ = SubscriptionType.objects.get_or_create(
            title="Silver",
            type=SubscriptionType.silver,
            price=30,
            payment_method=SubscriptionType.usd,
            duration=5
        )
        subscription, _ = Subscription.objects.get_or_create(
            user=user,
            type=subscription_type,
            expires_at=datetime.datetime(2022, 8, 20, 20) + datetime.timedelta(days=subscription_type.duration)
        )

        self.stdout.write(self.style.SUCCESS('Successfully create data'))
