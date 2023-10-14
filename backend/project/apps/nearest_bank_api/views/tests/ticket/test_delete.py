import pytest
from django.urls import reverse
from rest_framework.status import HTTP_204_NO_CONTENT
from project.apps.nearest_bank_api.services.sale_point import (
    sale_points_save_from_json_file,
)
from project.apps.nearest_bank_api.models import Service, SalePoint, Ticket


@pytest.mark.django_db
def test_valid_data(client):
    sale_points_save_from_json_file('/code/project/apps/nearest_bank_api/'
                                    'services/tests/sale_point/sale_point_test_data.json')

    service_to_add = Service.objects.first()
    sale_point_to_add = SalePoint.objects.first()
    ticket = Ticket.objects.create(
        salePoint=sale_point_to_add,
        service=service_to_add
    )
    ticket_id = ticket.id

    url = reverse('tickets_detail', kwargs={'ticket_id': ticket.id})

    response = client.delete(url)
    assert response.status_code == HTTP_204_NO_CONTENT

    assert not Ticket.objects.filter(id=ticket_id).exists()