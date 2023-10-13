from django.db.transaction import atomic
from rest_framework.serializers import ModelSerializer

from project.apps.nearest_bank_api.models import (
    OpenHours,
    OpenHoursIndividual,
    SalePoint,
)


class OpenHoursSerializer(ModelSerializer):
    class Meta:
        model = OpenHours
        fields = ['days', 'hours']


class OpenHoursIndividualSerializer(ModelSerializer):
    class Meta:
        model = OpenHoursIndividual
        fields = ['days', 'hours']


class SalePointSerializer(ModelSerializer):
    openHours = OpenHoursSerializer(many=True)
    openHoursIndividual = OpenHoursIndividualSerializer(many=True)

    class Meta:
        model = SalePoint
        fields = '__all__'

    @atomic
    def create(self, validated_data):
        open_hours_data = validated_data.pop('openHours')
        open_hours_individual_data = validated_data.pop('openHoursIndividual')

        sale_point = SalePoint.objects.create(**validated_data)

        open_hours_serializer = OpenHoursSerializer(data=open_hours_data, many=True)
        if open_hours_serializer.is_valid(raise_exception=True):
            open_hours_serializer.save(salePoint=sale_point)

        open_hours_individual_serializer = OpenHoursIndividualSerializer(
            data=open_hours_individual_data,
            many=True
        )
        if open_hours_individual_serializer.is_valid(raise_exception=True):
            open_hours_individual_serializer.save(salePoint=sale_point)

        return sale_point
