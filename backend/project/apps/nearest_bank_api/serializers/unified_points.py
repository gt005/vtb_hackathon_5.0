from rest_framework.serializers import (
    CharField,
    FloatField,
    IntegerField,
    Serializer,
    SerializerMethodField,
)

from project.apps.nearest_bank_api.models import Atm, SalePoint
from project.apps.nearest_bank_api.serializers.service import ServiceReadSerializer
from project.apps.nearest_bank_api.serializers.ticket import TicketReadSerializer


class UnifiedPoinsReadSerializer(Serializer):
    id = IntegerField()
    type = SerializerMethodField()
    latitude = FloatField()
    longitude = FloatField()
    address = CharField()
    salePointName = CharField(default=None)
    services = ServiceReadSerializer(many=True)
    serviceStaffAmount = IntegerField(default=None)
    tickets = SerializerMethodField()

    def get_type(self, obj: Atm | SalePoint) -> str:
        if isinstance(obj, Atm):
            return 'atm'
        elif isinstance(obj, SalePoint):
            return 'office'

        return ''

    def get_tickets(self, obj: Atm | SalePoint) -> list[dict] | None:
        if isinstance(obj, SalePoint):
            return TicketReadSerializer(obj.tickets, many=True).data

        return None
