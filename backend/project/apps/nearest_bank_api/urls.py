from django.urls import path

from project.apps.nearest_bank_api.views.department import DepartmentsListView
from project.apps.nearest_bank_api.views.service import ServiceListApi
from project.apps.nearest_bank_api.views.ticket import TicketListView, TicketDetailView


urlpatterns = [
    path('get-departments/', DepartmentsListView.as_view(), name='unified_points_list'),
    path('services/', ServiceListApi.as_view(), name='services_list'),
    path('tickets/', TicketListView.as_view(), name='tickets_list'),
    path('tickets/<int:ticket_id>', TicketDetailView.as_view(), name='tickets_detail'),
]
