import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK

from project.apps.nearest_bank_api.models import SalePoint, Service, Ticket
from project.apps.nearest_bank_api.services.atm import atms_save_from_json_file
from project.apps.nearest_bank_api.services.sale_point import (
    sale_points_save_from_json_file,
)


@pytest.mark.django_db
def test_api_response(client):
    sale_points_save_from_json_file('/code/project/apps/nearest_bank_api/'
                                    'services/tests/sale_point/sale_point_test_data.json')
    atms_save_from_json_file('/code/project/apps/nearest_bank_api/'
                             'services/tests/atm/atm_test_data.json')

    url = reverse('unified_points_list')

    response = client.get(url)
    assert response.status_code == HTTP_200_OK


@pytest.mark.django_db
def test_ticket(client):
    sale_points_save_from_json_file('/code/project/apps/nearest_bank_api/'
                                    'services/tests/sale_point/sale_point_test_data.json')

    service_to_add = Service.objects.first()

    for sale_point in SalePoint.objects.all():
        Ticket.objects.create(
            salePoint=sale_point,
            service=service_to_add
        )

    url = reverse('unified_points_list')

    response = client.get(url)
    assert response.status_code == HTTP_200_OK

    for sale_point in response.data:
        db_sale_point = SalePoint.objects.get(id=sale_point['id'])
        expected_tickets = [
            {
                'id': db_ticket.id,
                'service': db_ticket.service_id,
                'user_id': None,
                'salePoint': db_ticket.salePoint.id,
                'label': db_ticket.label
            }
            for db_ticket in db_sale_point.tickets.all()
        ]
        assert expected_tickets == sale_point['tickets']
