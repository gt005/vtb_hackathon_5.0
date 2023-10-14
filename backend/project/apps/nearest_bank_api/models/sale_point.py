from django.db import models
from project.apps.nearest_bank_api.models.common import PositionalEntity


class SalePoint(PositionalEntity, models.Model):
    salePointName = models.CharField(
        verbose_name='Наименование ТТ',
        max_length=255
    )
    salePointCode = models.CharField(
        verbose_name='Код ТП',
        max_length=255,
        null=True,
        blank=True
    )
    status = models.CharField(
        verbose_name='Статус ТП',
        max_length=255
    )
    rko = models.CharField(
        verbose_name='Наличие РКО',
        max_length=255,
        null=True,
        blank=True
    )
    network = models.CharField(
        verbose_name='Сеть',
        max_length=255,
        null=True,
        blank=True
    )
    officeType = models.CharField(
        verbose_name='Открытый тип офиса',
        max_length=255,
        null=True,
        blank=True
    )
    salePointFormat = models.CharField(
        verbose_name='Формат ТП',
        max_length=255,
        null=True,
        blank=True
    )
    suoAvailability = models.CharField(
        verbose_name='Наличие СУО',
        max_length=10,
        null=True,
        blank=True
    )
    hasRamp = models.CharField(
        verbose_name='Флаг наличия пандуса',
        max_length=10,
        null=True,
        blank=True
    )
    metroStation = models.CharField(
        verbose_name='Станция метро',
        max_length=500,
        null=True,
        blank=True
    )
    distance = models.IntegerField(
        verbose_name='Расстояние',
        null=True,
        blank=True
    )
    kep = models.BooleanField(
        verbose_name='Признак выдачи КЭП',
        null=True,
        blank=True
    )
    myBranch = models.BooleanField(
        verbose_name='Признак "Мое отделение"',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Отделение банка'


class OpenHours(models.Model):
    salePoint = models.ForeignKey(
        SalePoint,
        related_name='openHours',
        on_delete=models.CASCADE
    )
    days = models.CharField(
        verbose_name='День недели/Перерыв',
        max_length=50
    )
    hours = models.CharField(
        verbose_name='Время',
        max_length=50,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Рабочие часы для ЮЛ'


class OpenHoursIndividual(models.Model):
    salePoint = models.ForeignKey(
        SalePoint,
        related_name='openHoursIndividual',
        on_delete=models.CASCADE
    )
    days = models.CharField(
        verbose_name='День недели/Перерыв',
        max_length=50
    )
    hours = models.CharField(
        verbose_name='Время',
        max_length=50,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Рабочие часы для ФЛ'
