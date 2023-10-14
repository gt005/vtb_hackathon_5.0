from django.db import models

from project.apps.nearest_bank_api.models.asbtracts import (
    PositionalEntity,
    ServiceAdditionalInformation,
)
from project.apps.nearest_bank_api.models.common import Service


class Atm(PositionalEntity, models.Model):
    allDay = models.BooleanField(
        verbose_name='Работает круглосуточно',
        default=False
    )
    services = models.ManyToManyField(
        Service,
        through='AtmServiceThrough',
        related_name='atms'
    )

    class Meta:
        verbose_name = 'Банкомат'


class AtmServiceThrough(ServiceAdditionalInformation, models.Model):
    atm = models.ForeignKey(Atm, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сервис Банкомата через'
        unique_together = ["atm", "service"]
