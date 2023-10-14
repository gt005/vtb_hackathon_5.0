from rest_framework.response import Response
from rest_framework.views import APIView

from project.apps.nearest_bank_api.selectors.services import service_get_list
from project.apps.nearest_bank_api.serializers.service import ServiceReadSerializer


class ServiceListApi(APIView):
    output_serializer_class = ServiceReadSerializer

    def get(self, *args, **kwargs):
        data = self.output_serializer_class(service_get_list(), many=True).data

        return Response(data)
