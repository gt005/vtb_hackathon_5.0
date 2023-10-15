import random

from project.apps.nearest_bank_api.domain.emums import ServiceNameEnum

# Используется для создания базы, поэтому используется просто словарь
# А так, должны браться из базы банка при создании миграций в данном проекте
AVERAGE_WAIT_TIME_FOR_SERVICE = {
    tag.name: 3 + random.random() * 30 for tag in ServiceNameEnum
}

SERVICES_ONLINE_TEXT = {
    'takeLoan': 'Кредит можно взять в приложении банка на главной странице на вкладке "Кредит"',
    'openCard': 'Карту можно открыть на главной странице банка'
}

SERVICES_DESCRIPTION = {
    'supportsChargeRub': 'Возможность обменять наличные рубли на наличную иностранную валюту',
    'openCard': 'Возможность открытия дебетовой карты'
}
