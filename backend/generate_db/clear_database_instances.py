import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

django.setup()
from project.apps.nearest_bank_api.models import SalePoint, Atm

def clear_database_instances():
    SalePoint.objects.all().delete()
    Atm.objects.all().delete()


if __name__ == '__main__':
    clear_database_instances()
