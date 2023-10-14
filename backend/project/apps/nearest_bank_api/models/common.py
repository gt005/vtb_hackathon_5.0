from django.db import models


class PositionalEntity(models.Model):
    address = models.CharField(
        verbose_name='Адрес',
        max_length=400,
        null=True,
        blank=True
    )
    latitude = models.FloatField(
        verbose_name='Географическая широта'
    )
    longitude = models.FloatField(
        verbose_name='Географическая долгота'
    )

    class Meta:
        abstract = True
