import datetime as date

from django.core.validators import MaxValueValidator, MinValueValidator


def birthday_validators():
    return [
        MinValueValidator(limit_value=date.date(1900, 1, 1)),
        MaxValueValidator(limit_value=date.date.today)
    ]


def age_validators():
    return [
        MinValueValidator(8),
        MaxValueValidator(100)
    ]
