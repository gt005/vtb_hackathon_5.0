from django.db.transaction import atomic
from rest_framework.serializers import Serializer, CharField, FloatField, IntegerField, SerializerMethodField
from project.apps.nearest_bank_api.serializers.service import ServiceReadSerializer
from project.apps.nearest_bank_api.models import Atm, SalePoint


class UnifiedPoinsReadSerializer(Serializer):
    type = SerializerMethodField()
    latitude = FloatField()
    longitude = FloatField()
    address = CharField()
    salePointName = CharField(default=None)
    workload = IntegerField(default=0)
    services = ServiceReadSerializer(many=True)

    def get_type(self, obj: Atm | SalePoint) -> str:
        if isinstance(obj, Atm):
            return 'atm'
        elif isinstance(obj, SalePoint):
            return 'office'

        return ''
