from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

# local imports
from .serializers import ShipmentSerializer
from .models import Shipment


class ShipmentView(generics.ListAPIView):
    """
    Used to list shipments
    """

    queryset = Shipment.objects.all()
    serializer_class = ShipmentSerializer
    lookup_field = "tracking_number"
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["tracking_number", "carrier"]
