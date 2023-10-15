from django.db.transaction import atomic

from project.apps.nearest_bank_api.models import SalePoint, Service, Ticket


@atomic
def ticket_create(*, user_id: int, label: str, salePoint: SalePoint, service: Service) -> Ticket:
    return Ticket.objects.create(
        user_id=user_id,
        label=label,
        salePoint=salePoint,
        service=service
    )


@atomic
def ticket_delete(*, ticket: Ticket) -> None:
    ticket.delete()
