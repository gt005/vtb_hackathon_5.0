from django.db import models

from project.apps.nearest_bank_api.domain.emums import ServiceNameEnum


class Service(models.Model):
    name = models.CharField(
        verbose_name='Имя сервиса',
        max_length=50,
        choices=[(tag.value, tag.name) for tag in ServiceNameEnum],
        unique=True
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    onlineText = models.TextField(
        verbose_name='Онлайн текст',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Предоставляемый сервис'
