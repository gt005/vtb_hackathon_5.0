import json

import pytest
from django.forms.models import model_to_dict

from project.apps.nearest_bank_api.models.sale_point import (
    OpenHours,
    OpenHoursIndividual,
    SalePoint,
)
from project.apps.nearest_bank_api.services.sale_point import (
    sale_points_save_from_json_file,
)


@pytest.mark.django_db
def test_valid_case():
    json_file_name = ('/code/project/apps/nearest_bank_api'
                     '/services/tests/sale_point/sale_point_test_data.json')

    sale_points_save_from_json_file(json_file_name)

    with open(json_file_name, 'r') as file:
        sale_points_data = json.load(file)

    for data in sale_points_data:
        sale_point = SalePoint.objects.get(salePointName=data['salePointName'])
        sale_point_dict = model_to_dict(
            sale_point,
            exclude=["id", "openHours", "openHoursIndividual"]
        )

        # Удаление ключей со значением None, которых нет в исходном JSON
        sale_point_dict = {k: v for k, v in sale_point_dict.items() if v is not None or k in data}

        expected_dict = {
            k: v for k, v in data.items() if k not in ["openHours", "openHoursIndividual"]
        }

        assert sale_point_dict == expected_dict

        for open_hours in data['openHours']:
            assert OpenHours.objects.filter(salePoint=sale_point, **open_hours).exists()

        for open_hours_individual in data['openHoursIndividual']:
            assert OpenHoursIndividual.objects.filter(
                salePoint=sale_point,
                **open_hours_individual
            ).exists()
