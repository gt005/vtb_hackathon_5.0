from django.contrib import admin

from project.apps.nearest_bank_api.models import (
    Atm,
    SalePoint,
    SalePointServiceThrough,
    Service,
    Ticket,
)

admin.site.register(Service)
admin.site.register(SalePoint)
admin.site.register(Atm)
admin.site.register(Ticket)
admin.site.register(SalePointServiceThrough)
