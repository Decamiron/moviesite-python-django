from django.db import models
from users.models import MyUser


class SubscriptionType(models.Model):
    silver = 'silver'
    gold = 'gold'

    SUBSCRIPTION_TYPES = (
        (silver, "Silver"),
        (gold, "Gold")
    )

    usd = "usd"
    grn = "grn"
    euro = "euro"

    PAYMENTS_METHODS = (
        (usd, "USD"),
        (grn, "Grivna"),
        (euro, "Euro"),
    )

    title = models.CharField(max_length=10)
    type = models.CharField(choices=SUBSCRIPTION_TYPES, max_length=10)
    price = models.PositiveIntegerField()
    payment_method = models.CharField(choices=PAYMENTS_METHODS, max_length=7)
    duration = models.PositiveIntegerField(help_text="Duration in days")

    def __str__(self):
        return f"{self.title} - {self.type}"

    class Meta:
        verbose_name = "Тип подписки"
        verbose_name_plural = "Типы подписок"
        permissions = (
            ("color_username", "Have a color username"),
            ("can_create_public_film_room", "Can create public film rooms"),
            ("can_create_private_film_room", "Can create private film rooms"),
            ("can_watch_movies_in_advance", "Can watch movies in advance"),
        )


class Subscription(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="subscription")
    type = models.ForeignKey(SubscriptionType, on_delete=models.SET_NULL, null=True, related_name="subscription_type")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    expires_at = models.DateField()

    def get_subscription_type(self):
        return self.type

    def __str__(self):
        return f"{self.user.username} - {self.type}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
