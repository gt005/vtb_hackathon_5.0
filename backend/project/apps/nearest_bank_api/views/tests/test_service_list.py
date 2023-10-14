import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK

from project.apps.nearest_bank_api.models import Service


@pytest.mark.django_db
def test_api_response(client):
    url = reverse('services_list')

    response = client.get(url)
    assert response.status_code == HTTP_200_OK

    for service in Service.objects.all():
        assert {
            'id': service.id,
            'name': service.name,
            'description': service.description,
            'onlineText': service.onlineText,
            'averageWaitTime': service.averageWaitTime
        } in response.data
