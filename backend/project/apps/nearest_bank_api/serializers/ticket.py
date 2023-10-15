from rest_framework.serializers import ModelSerializer

from project.apps.nearest_bank_api.models import Ticket


class TicketReadSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'label', 'user_id', 'salePoint', 'service')


class TicketCreateSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('user_id', 'label', 'salePoint', 'service')
