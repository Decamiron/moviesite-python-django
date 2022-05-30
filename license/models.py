from django.db import models


class License(models.Model):
    title = models.CharField(max_length=24)
    code = models.CharField(max_length=100, unique=True, db_index=True)

    def get_license(self):
        return True

    class Meta:
        verbose_name = "Лицензия"
        verbose_name_plural = "Лицензии"
