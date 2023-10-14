from django.db.transaction import atomic
from rest_framework.serializers import ModelSerializer

from project.apps.nearest_bank_api.models.sale_point import (
    OpenHours,
    OpenHoursIndividual,
    SalePoint,
)


class OpenHoursCreateSerializer(ModelSerializer):
    class Meta:
        model = OpenHours
        fields = ('days', 'hours')


class OpenHoursIndividualCreateSerializer(ModelSerializer):
    class Meta:
        model = OpenHoursIndividual
        fields = ('days', 'hours')


class SalePointCreateSerializer(ModelSerializer):
    openHours = OpenHoursCreateSerializer(many=True)
    openHoursIndividual = OpenHoursIndividualCreateSerializer(many=True)

    class Meta:
        model = SalePoint
        fields = '__all__'

    @atomic
    def create(self, validated_data: dict) -> SalePoint:
        open_hours_data = validated_data.pop('openHours')
        open_hours_individual_data = validated_data.pop('openHoursIndividual')

        sale_point = SalePoint.objects.create(**validated_data)

        open_hours_serializer = OpenHoursCreateSerializer(data=open_hours_data, many=True)
        if open_hours_serializer.is_valid(raise_exception=True):
            open_hours_serializer.save(salePoint=sale_point)

        open_hours_individual_serializer = OpenHoursIndividualCreateSerializer(
            data=open_hours_individual_data,
            many=True
        )
        if open_hours_individual_serializer.is_valid(raise_exception=True):
            open_hours_individual_serializer.save(salePoint=sale_point)

        return sale_point
