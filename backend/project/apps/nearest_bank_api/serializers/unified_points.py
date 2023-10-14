from rest_framework.serializers import (
    CharField,
    FloatField,
    IntegerField,
    Serializer,
    SerializerMethodField,
)

from project.apps.nearest_bank_api.models import Atm, SalePoint
from project.apps.nearest_bank_api.selectors.unified_points import (
    unified_point_get_service_id_list,
)
from project.apps.nearest_bank_api.serializers.ticket import TicketReadSerializer
from project.apps.nearest_bank_api.serializers.sale_point import OpenHoursCreateSerializer


class UnifiedPoinsReadSerializer(Serializer):
    id = IntegerField()
    type = SerializerMethodField()
    latitude = FloatField()
    longitude = FloatField()
    address = CharField()
    salePointName = CharField(default=None)
    services = SerializerMethodField()
    serviceStaffAmount = IntegerField(default=None)
    tickets = SerializerMethodField()
    openHours = SerializerMethodField()

    def get_type(self, obj: Atm | SalePoint) -> str:
        if isinstance(obj, Atm):
            return 'atm'
        elif isinstance(obj, SalePoint):
            return 'office'

        return ''

    def get_services(self, obj: Atm | SalePoint) -> list[int]:
        return unified_point_get_service_id_list(unified_point=obj)

    def get_tickets(self, obj: Atm | SalePoint) -> list[dict] | None:
        if isinstance(obj, SalePoint):
            return TicketReadSerializer(obj.tickets, many=True).data

        return None

    def get_openHours(self, obj: Atm | SalePoint) -> list[dict] | None:
        if isinstance(obj, SalePoint):
            return OpenHoursCreateSerializer(obj.openHours.all(), many=True).data

        return None
