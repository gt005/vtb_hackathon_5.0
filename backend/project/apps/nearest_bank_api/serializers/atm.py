from django.db.transaction import atomic
from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    Serializer,
    ValidationError,
)

from project.apps.nearest_bank_api.models.atm import Atm, AtmServiceThrough
from project.apps.nearest_bank_api.models.common import Service
from project.apps.nearest_bank_api.domain.emums import ServiceNameEnum


class AtmServiceThroughCreateSerializer(Serializer):
    name = CharField()
    serviceCapability = CharField()
    serviceActivity = CharField()


class AtmCreateSerializer(ModelSerializer):
    services = AtmServiceThroughCreateSerializer(many=True)

    class Meta:
        model = Atm
        fields = '__all__'

    def to_internal_value(self, data):
        if 'services' not in data:
            raise ValidationError({'services': ['This field is required.']})

        if not isinstance(data['services'], dict):  # Если уже на сохранение идет
            return super().to_internal_value(data)

        services_data = data.pop('services')
        services_list = [{'name': key, **value} for key, value in services_data.items()]
        data['services'] = services_list
        return super().to_internal_value(data)

    @atomic
    def create(self, validated_data: dict) -> Atm:
        services = validated_data.pop('services')

        atm = Atm.objects.create(**validated_data)

        for service_data in services:
            service = Service.objects.get_or_create(
                name=ServiceNameEnum[service_data['name']].value
            )[0]
            AtmServiceThrough.objects.create(
                atm=atm,
                service=service,
                serviceCapability=service_data['serviceCapability'],
                serviceActivity=service_data['serviceActivity']
            )

        return atm


class ATMListSerializer(Serializer):
    atms = AtmCreateSerializer(many=True)

    def create(self, validated_data):
        atms_data = validated_data.pop('atms')

        atms_serializer = AtmCreateSerializer(data=atms_data, many=True)
        atms_serializer.is_valid(raise_exception=True)
        created_atms = atms_serializer.save()

        return {"atms": created_atms}
