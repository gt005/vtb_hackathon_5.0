# Для обозначения нахождения django моделей и настроек
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()


import random
from django.db import IntegrityError
from project.apps.nearest_bank_api.models import SalePointServiceThrough, SalePoint, Service
from project.apps.nearest_bank_api.domain.emums import ServiceActivityEnum


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
            print(f'Combination of sale_point: {sale_point.id} and service: {service.id} already exists.')
            continue

    print(f'{entries} SalePointServiceThrough objects created.')


if __name__ == '__main__':
    create_sale_point_service_through(len(SalePoint.objects.all()) * 3)