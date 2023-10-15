from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from project.apps.nearest_bank_api.models import Ticket
from project.apps.nearest_bank_api.serializers.ticket import (
    TicketCreateSerializer,
    TicketReadSerializer,
)
from project.apps.nearest_bank_api.services.ticket import ticket_create, ticket_delete


class TicketListView(APIView):
    input_serializer_class = TicketCreateSerializer
    output_serializer_class = TicketReadSerializer

    def post(self, *agrs, **kwargs):
        serializer = self.input_serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        ticket = ticket_create(**serializer.validated_data)

        return Response(
            self.output_serializer_class(instance=ticket).data,
            status=status.HTTP_201_CREATED
        )


class TicketDetailView(APIView):
    def delete(self, request, ticket_id: int, *agrs, **kwargs):
        print(ticket_id)
        ticket = get_object_or_404(Ticket, id=ticket_id)

        ticket_delete(ticket=ticket)

        return Response(status=status.HTTP_204_NO_CONTENT)
