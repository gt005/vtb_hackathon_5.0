import pytest
from django.urls import reverse
from rest_framework.status import HTTP_201_CREATED
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

    test_data = {
        'user_id': 4223,
        'salePoint': sale_point_to_add.id,
        'service': service_to_add.id
    }

    url = reverse('tickets_list')

    response = client.post(
        url,
        data=test_data
    )
    assert response.status_code == HTTP_201_CREATED

    assert Ticket.objects.filter(
        user_id=test_data['user_id'],
        salePoint=sale_point_to_add,
        service=service_to_add
    ).exists()