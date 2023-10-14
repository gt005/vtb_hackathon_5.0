from project.apps.nearest_bank_api.models import Atm, SalePoint
from project.apps.nearest_bank_api.selectors.atm import atm_get_list
from project.apps.nearest_bank_api.selectors.sale_points import sale_point_get_list


def get_unified_points_queryset() -> list[Atm | SalePoint]:
    # Функция для объединения двух queryset в один список
    unified_list = list(sale_point_get_list()) + list(atm_get_list())
    return unified_list
