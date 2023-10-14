import random

from project.apps.nearest_bank_api.domain.emums import ServiceNameEnum

# Используется для создания базы, поэтому используется просто словарь
# А так, должны браться из базы банка при создании миграций в данном проекте
AVERAGE_WAIT_TIME_FOR_SERVICE = {
    tag.name: 3 + random.random() * 30 for tag in ServiceNameEnum
}
