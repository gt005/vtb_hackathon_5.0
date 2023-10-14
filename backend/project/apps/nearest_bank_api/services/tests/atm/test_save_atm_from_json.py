import json

import pytest
from django.forms.models import model_to_dict

from project.apps.nearest_bank_api.models.atm import Atm, AtmServiceThrough
from project.apps.nearest_bank_api.services.atm import atms_save_from_json_file


@pytest.mark.django_db
def test_valid_case():
    json_file_name = ('/code/project/apps/nearest_bank_api/services/tests/atm/atm_test_data.json')

    atms_save_from_json_file(json_file_name)

    with open(json_file_name, 'r') as file:
        atm_json_data = json.load(file)['atms']

    for data in atm_json_data:
        atm = Atm.objects.get(address=data['address'])
        atm_dict = model_to_dict(
            atm,
            exclude=["id", "services"]
        )

        # Удаление ключей со значением None, которых нет в исходном JSON
        atm_dict = {k: v for k, v in atm_dict.items() if v is not None or k in data}

        expected_dict = {
            k: v for k, v in data.items() if k not in ["services"]
        }

        assert atm_dict == expected_dict

        for service_name, service_availability in data['services'].items():
            assert AtmServiceThrough.objects.filter(
                atm=atm,
                service__name=service_name,
                **service_availability
            ).exists()
