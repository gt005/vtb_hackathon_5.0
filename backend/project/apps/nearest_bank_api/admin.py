from django.contrib import admin
from project.apps.nearest_bank_api.models import Service, SalePoint, Atm, Ticket, SalePointServiceThrough

admin.site.register(Service)
admin.site.register(SalePoint)
admin.site.register(Atm)
admin.site.register(Ticket)
admin.site.register(SalePointServiceThrough)
