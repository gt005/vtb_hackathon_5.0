from enum import Enum


class ServiceNameEnum(Enum):
    supportsEur = ('Работа с Евро')
    supportsRub = ('Работа с Рублями')
    supportsUsd = ('Работа с Долларами')
    supportsChargeRub = ('Поддержка зарядки рублей')
    blind = ('Услуги для слепых')
    nfcForBankCards = ('Поддержка NFC для банковских карт')
    qrRead = ('Чтение QR-кодов')
    wheelchair = ('Доступность для инвалидных колясок')


class ServiceCapabilityEnum(Enum):
    SUPPORTED = 'SUPPORTED'
    UNKNOWN = 'UNKNOWN'
    UNSUPPORTED = 'UNSUPPORTED'


class ServiceActivityEnum(Enum):
    AVAILABLE = 'AVAILABLE'
    UNAVAILABLE = 'UNAVAILABLE'
    UNKNOWN = 'UNKNOWN'
