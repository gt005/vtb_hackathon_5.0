from project.apps.nearest_bank_api.models import Ticket, SalePoint, Service
from django.db.transaction import atomic


@atomic
def ticket_create(*, user_id: int, salePoint: SalePoint, service: Service) -> Ticket:
    return Ticket.objects.create(user_id=user_id, salePoint=salePoint, service=service)


@atomic
def ticket_delete(*, ticket: Ticket) -> None:
    ticket.delete()
