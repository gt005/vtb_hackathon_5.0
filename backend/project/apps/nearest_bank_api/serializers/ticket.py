from rest_framework.serializers import ModelSerializer

from project.apps.nearest_bank_api.models import Ticket


class TicketReadSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'service')
