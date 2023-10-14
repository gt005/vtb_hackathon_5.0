from django.db.models import QuerySet, Prefetch
from project.apps.nearest_bank_api.models import SalePoint, Service


def sale_point_get_list() -> QuerySet[SalePoint]:
    return SalePoint.objects.all().prefetch_related(
        Prefetch(
            'services',
            queryset=Service.objects.all(),
        )
    )
