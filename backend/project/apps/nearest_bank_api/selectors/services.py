from django.db.models import QuerySet

from project.apps.nearest_bank_api.models import Service


def service_get_list() -> QuerySet:
    return Service.objects.all()
