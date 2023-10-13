if __name__ == '__main__':
    # Для обозначения нахождения django моделей и настроек
    import os

    import django

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

    django.setup()

import json

from django.db.transaction import atomic

from project.apps.nearest_bank_api.serializers.sale_point import SalePointSerializer


@atomic
def sale_points_save_from_json_file(path_to_file: str) -> None:
    with open(path_to_file, 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        sale_point_serializer = SalePointSerializer(data=json_data, many=True)

        sale_point_serializer.is_valid(raise_exception=True)
        sale_point_serializer.save()


if __name__ == '__main__':
    sale_points_save_from_json_file(
        '/code/datasets/offices.json'
    )
