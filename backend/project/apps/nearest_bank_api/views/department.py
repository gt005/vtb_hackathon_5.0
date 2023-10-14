from rest_framework.views import APIView
from project.apps.nearest_bank_api.serializers.unified_points import UnifiedPoinsReadSerializer
from rest_framework.response import Response
from project.apps.nearest_bank_api.selectors.unified_points import get_unified_points_queryset


class DepartmentsListView(APIView):
    output_serializer_class = UnifiedPoinsReadSerializer

    def get(self):
        data = self.output_serializer_class(get_unified_points_queryset(), many=True).data

        return Response(data)
