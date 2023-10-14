from django.db.transaction import atomic
from rest_framework.serializers import ModelSerializer, Serializer, ValidationError

from project.apps.nearest_bank_api.models.atm import Atm, AtmService


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = AtmService
        fields = ('name', 'serviceCapability', 'serviceActivity')


class AtmCreateSerializer(ModelSerializer):
    services = ServiceSerializer(many=True)

    class Meta:
        model = Atm
        fields = '__all__'

    def to_internal_value(self, data):
        if 'services' not in data:
            raise ValidationError({'services': ['This field is required.']})

        if not isinstance(data['services'], dict):
            return super().to_internal_value(data)

        services_data = data.pop('services')
        services_list = [{'name': key, **value} for key, value in services_data.items()]
        data['services'] = services_list
        return super().to_internal_value(data)

    def create(self, validated_data: dict) -> Atm:
        services = validated_data.pop('services')

        atm = Atm.objects.create(**validated_data)

        services_serializer = ServiceSerializer(data=services, many=True)
        if services_serializer.is_valid(raise_exception=True):
            services_serializer.save(atm=atm)

        return atm


class ATMListSerializer(Serializer):
    atms = AtmCreateSerializer(many=True)

    def create(self, validated_data):
        atms_data = validated_data.pop('atms')

        atms_serializer = AtmCreateSerializer(data=atms_data, many=True)
        atms_serializer.is_valid(raise_exception=True)
        created_atms = atms_serializer.save()

        return {"atms": created_atms}