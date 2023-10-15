# Для обозначения нахождения django моделей и настроек
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()

import random

from django.db import IntegrityError
from faker import Faker

from project.apps.nearest_bank_api.domain.emums import ServiceActivityEnum
from project.apps.nearest_bank_api.models import (
    SalePoint,
    SalePointServiceThrough,
    Service,
    Ticket,
)
from project.apps.nearest_bank_api.selectors.unified_points import (
    unified_point_get_active_service_id_list,
)

fake = Faker("ru_RU")


def create_sale_point_service_through(entries=100):
    all_services = list(Service.objects.all())
    all_sale_points = list(SalePoint.objects.all())

    if not all_services or not all_sale_points:
        print('No data for services or sale points. Please make sure they are populated.')
        return

    for _ in range(entries):
        service = random.choice(all_services)
        sale_point = random.choice(all_sale_points)

        try:
            SalePointServiceThrough.objects.create(
                sale_point=sale_point,
                service=service,
                serviceActivity=ServiceActivityEnum.AVAILABLE.value
            )
        except IntegrityError:
            continue

    print(f'{entries} SalePointServiceThrough objects created.')


def create_ticket(entries=100):
    all_services = list(Service.objects.all())
    all_sale_points = list(SalePoint.objects.all())

    if not all_services or not all_sale_points:
        print('No data for services or sale points. Please make sure they are populated.')
        return

    for _ in range(entries):
        sale_point = random.choice(all_sale_points)
        if not unified_point_get_active_service_id_list(unified_point=sale_point):
            continue

        service = random.choice(sale_point.services.all())

        try:
            Ticket.objects.create(
                label=fake.sentence(),
                user_id=random.randint(1, 1_000_000),
                salePoint=sale_point,
                service=service,
            )
        except IntegrityError:
            continue

    print(f'{entries} SalePointServiceThrough objects created.')


if __name__ == '__main__':
    print('Началась генерация сервисов у SalePoint')
    create_sale_point_service_through(len(SalePoint.objects.all()) * 3)
    print('Началась генерация тикетов')
    create_ticket(len(SalePoint.objects.all()) * 5)
