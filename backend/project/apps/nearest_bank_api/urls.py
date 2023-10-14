from django.urls import path
from project.apps.nearest_bank_api.views.department import DepartmentsListView

urlpatterns = [
    path('get-departments', DepartmentsListView.as_view(), name='unified_points_list'),
]
