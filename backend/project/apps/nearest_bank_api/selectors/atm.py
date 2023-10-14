from django.db.models import Prefetch, QuerySet

from project.apps.nearest_bank_api.models import Atm, Service


def atm_get_list() -> QuerySet[Atm,]:
    return Atm.objects.all().prefetch_related(
        Prefetch(
            'services',
            queryset=Service.objects.all(),
        )
    )
