if __name__ == '__main__':
    # Для обозначения нахождения django моделей и настроек
    import os

    import django

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

    django.setup()

import json

from django.db.transaction import atomic

from project.apps.nearest_bank_api.serializers.atm import ATMListSerializer


@atomic
def atms_save_from_json_file(path_to_file: str) -> None:
    with open(path_to_file, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        atm_serializer = ATMListSerializer(data=json_data)

        atm_serializer.is_valid(raise_exception=True)
        atm_serializer.save()


if __name__ == '__main__':
    atms_save_from_json_file(
        '/code/datasets/atms.json'
    )
