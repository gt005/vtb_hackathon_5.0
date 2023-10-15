OFFICES_FILE_NAME = '/code/datasets/offices.json'
ATMS_FILE_NAME = '/code/datasets/atms.json'


if __name__ == '__main__':
    # Для обозначения нахождения django моделей и настроек
    import os

    import django

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

    django.setup()

    from project.apps.nearest_bank_api.services.atm import atms_save_from_json_file
    from project.apps.nearest_bank_api.services.sale_point import (
        sale_points_save_from_json_file,
    )
    print('Парсинг Sale Point начался')
    sale_points_save_from_json_file(OFFICES_FILE_NAME)
    print('Парсинг Atm начался')
    atms_save_from_json_file(ATMS_FILE_NAME)
