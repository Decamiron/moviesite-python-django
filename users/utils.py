from datetime import date

from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


def get_date_validators():
    return [
        MinValueValidator(limit_value=datetime.date.today() - datetime.timedelta(days=100*365)),
        MaxValueValidator(limit_value=datetime.date.today() - datetime.timedelta(days=18*365))
    ]


def get_age_validators():
    return [
        MinValueValidator(18),
        MaxValueValidator(100)
    ]