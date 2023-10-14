from django.db import models
from project.apps.nearest_bank_api.models.common import PositionalEntity
from project.apps.nearest_bank_api.domain.emums import ServiceActivityEnum, ServiceCapabilityEnum, ServiceNameEnum


class Atm(PositionalEntity, models.Model):
    allDay = models.BooleanField(
        verbose_name='Работает круглосуточно',
        default=False
    )

    class Meta:
        verbose_name = 'Банкомат'


class AtmService(models.Model):
    atm = models.ForeignKey(to=Atm, related_name='services', on_delete=models.CASCADE)
    name = models.CharField(
        verbose_name='Имя сервиса',
        choices=[(tag.value, tag.name) for tag in ServiceNameEnum],
        max_length=50
    )

    serviceCapability = models.CharField(
        max_length=50,
        choices=[(tag.value, tag.name) for tag in ServiceCapabilityEnum]
    )

    serviceActivity = models.CharField(
        max_length=50,
        choices=[(tag.value, tag.name) for tag in ServiceActivityEnum]
    )

    class Meta:
        verbose_name = 'Сервис банкомата'
        unique_together = ["atm", "name"]
