from rest_framework.serializers import ModelSerializer

# local imports
from .models import Shipment, Location


class LocationSerializer(ModelSerializer):
    """This class used to serialize the Location model"""

    class Meta:
        model = Location
        fields = (
            "line1",
            "city_name",
            "zip_code",
            "country_name",
            "weather",
        )


class ShipmentSerializer(ModelSerializer):
    """This class used to serialize the shipment model"""

    sender_address = LocationSerializer()
    receiver_address = LocationSerializer()

    class Meta:
        model = Shipment
        fields = (
            "tracking_number",
            "carrier",
            "sender_address",
            "receiver_address",
            "article_name",
            "article_quantity",
            "article_price",
            "sku",
            "status",
        )
