from rest_framework.response import Response
from rest_framework.views import APIView

from project.apps.nearest_bank_api.selectors.unified_points import (
    unified_points_get_queryset,
)
from project.apps.nearest_bank_api.serializers.unified_points import (
    UnifiedPoinsReadSerializer,
)


class DepartmentsListView(APIView):
    output_serializer_class = UnifiedPoinsReadSerializer

    def get(self, *args, **kwargs):
        data = self.output_serializer_class(unified_points_get_queryset(), many=True).data

        return Response(data)
