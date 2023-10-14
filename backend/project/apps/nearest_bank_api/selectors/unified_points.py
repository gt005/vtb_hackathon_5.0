from project.apps.nearest_bank_api.models import Atm, SalePoint
from project.apps.nearest_bank_api.selectors.atm import atm_get_list
from project.apps.nearest_bank_api.selectors.sale_points import sale_point_get_list
from project.apps.nearest_bank_api.domain.emums import ServiceActivityEnum


def unified_points_get_queryset() -> list[Atm | SalePoint]:
    # Функция для объединения двух queryset в один список
    unified_list = list(sale_point_get_list()) + list(atm_get_list())
    return unified_list


def unified_point_get_service_id_list(unified_point: Atm | SalePoint) -> list[int]:
    if isinstance(unified_point, Atm):
        available_services = unified_point.services.filter(
            atmservicethrough__serviceActivity=ServiceActivityEnum.AVAILABLE.value
        )
    elif isinstance(unified_point, SalePoint):
        available_services = unified_point.services.filter(
            salepointservicethrough__serviceActivity=ServiceActivityEnum.AVAILABLE.value
        )

    return available_services.values_list('id', flat=True)
