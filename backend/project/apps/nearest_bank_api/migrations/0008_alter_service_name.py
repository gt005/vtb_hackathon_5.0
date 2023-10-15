# Generated by Django 4.2.6 on 2023-10-14 23:21

from django.db import migrations, models

from project.apps.nearest_bank_api.domain.emums import ServiceNameEnum
from project.apps.nearest_bank_api.models.consts import AVERAGE_WAIT_TIME_FOR_SERVICE, SERVICES_ONLINE_TEXT, SERVICES_DESCRIPTION


def fill_service_average_time(apps, schema_editor):
    Service = apps.get_model('nearest_bank_api', 'Service')
    services = []
    for service_name in ServiceNameEnum:
        service = Service.objects.get_or_create(name=service_name.value)[0]
        service.averageWaitTime = AVERAGE_WAIT_TIME_FOR_SERVICE[service_name.name]
        if service_name.name in SERVICES_ONLINE_TEXT:
            service.onlineText = SERVICES_ONLINE_TEXT[service_name.name]
        if service_name.name in SERVICES_DESCRIPTION:
            service.description = SERVICES_DESCRIPTION[service_name.name]
        services.append(service)

    Service.objects.bulk_update(services, ('averageWaitTime', 'onlineText', 'description'))


class Migration(migrations.Migration):

    dependencies = [
        ('nearest_bank_api', '0007_ticket_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(choices=[('Работа с Евро', 'supportsEur'), ('Работа с Рублями', 'supportsRub'), ('Работа с Долларами', 'supportsUsd'), ('Поддержка обмена валюты', 'supportsChargeRub'), ('Услуги для слепых', 'blind'), ('Поддержка NFC для банковских карт', 'nfcForBankCards'), ('Чтение QR-кодов', 'qrRead'), ('Доступность для инвалидных колясок', 'wheelchair'), ('Возможность открытия карты', 'openCard'), ('Возможность взятия потребительского кредита', 'takeLoan'), ('Возможность взятия ипотеки', 'takeMortgage')], max_length=50, unique=True, verbose_name='Имя сервиса'),
        ),
        migrations.RunPython(fill_service_average_time)
    ]