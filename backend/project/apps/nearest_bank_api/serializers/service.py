from rest_framework.serializers import ModelSerializer
from project.apps.nearest_bank_api.models import Service


class ServiceReadSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'name', 'description', 'onlineText')
