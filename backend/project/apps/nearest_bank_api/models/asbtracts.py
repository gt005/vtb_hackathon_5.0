from django.db import models

from project.apps.nearest_bank_api.domain.emums import (
    ServiceActivityEnum,
    ServiceCapabilityEnum,
)


class ServiceAdditionalInformation(models.Model):
    serviceCapability = models.CharField(
        max_length=50,
        choices=[(tag.value, tag.name) for tag in ServiceCapabilityEnum],
    )
    serviceActivity = models.CharField(
        max_length=50,
        choices=[(tag.value, tag.name) for tag in ServiceActivityEnum],
    )

    class Meta:
        abstract = True


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
