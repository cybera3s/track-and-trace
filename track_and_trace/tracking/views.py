from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response

# local imports
from .serializers import ShipmentSerializer
from .models import Shipment


class ShipmentView(generics.ListAPIView):
    """
    Used to list shipments
    """

    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tracking_number", "carrier"]

    def list(self, request, *args, **kwargs):

        # Make query params required
        tracking_number = self.request.query_params.get('tracking_number', None)
        carrier = self.request.query_params.get('carrier', None)
        if not (tracking_number or carrier):
            return Response([])

        return super().list(request, *args, **kwargs)

