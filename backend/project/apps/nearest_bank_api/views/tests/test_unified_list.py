import json
import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK
from project.apps.nearest_bank_api.services.sale_point import sale_points_save_from_json_file
from project.apps.nearest_bank_api.services.atm import atms_save_from_json_file


@pytest.mark.django_db
def test_api_response(client):
    sale_points_save_from_json_file('/code/project/apps/nearest_bank_api/'
                                    'services/tests/sale_point/sale_point_test_data.json')
    atms_save_from_json_file('/code/project/apps/nearest_bank_api/'
                             'services/tests/atm/atm_test_data.json')

    url = reverse('unified_points_list')

    response = client.get(url)

    assert response.status_code == HTTP_200_OK
