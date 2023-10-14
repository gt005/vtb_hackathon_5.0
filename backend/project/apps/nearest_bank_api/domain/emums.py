from enum import Enum


class ServiceNameEnum(Enum):
    supportsEur = "supportsEur"
    supportsRub = "supportsRub"
    supportsUsd = "supportsUsd"
    supportsChargeRub = "supportsChargeRub"
    blind = "blind"
    nfcForBankCards = "nfcForBankCards"
    qrRead = "qrRead"
    wheelchair = "wheelchair"


class ServiceCapabilityEnum(Enum):
    SUPPORTED = "SUPPORTED"
    UNKNOWN = "UNKNOWN"
    UNSUPPORTED = "UNSUPPORTED"


class ServiceActivityEnum(Enum):
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"
    UNKNOWN = "UNKNOWN"
