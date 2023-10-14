from django.urls import path

from project.apps.nearest_bank_api.views.department import DepartmentsListView
from project.apps.nearest_bank_api.views.service import ServiceListApi

urlpatterns = [
    path('get-departments/', DepartmentsListView.as_view(), name='unified_points_list'),
    path('services/', ServiceListApi.as_view(), name='services_list'),
]
