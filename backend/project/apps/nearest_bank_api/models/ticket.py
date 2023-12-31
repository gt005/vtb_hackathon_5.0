from django.db import models

from project.apps.nearest_bank_api.models import SalePoint, Service


class Ticket(models.Model):
    label = models.CharField(
        verbose_name='Заметка о тикете',
        max_length=255
    )
    user_id = models.IntegerField(
        verbose_name='id пользователя',
        null=True
    )
    salePoint = models.ForeignKey(
        SalePoint,
        verbose_name='Взят для отделения',
        related_name='tickets',
        on_delete=models.CASCADE
    )
    service = models.ForeignKey(
        Service,
        verbose_name='Тип операции',
        related_name='tickets',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Талон в отделении'
