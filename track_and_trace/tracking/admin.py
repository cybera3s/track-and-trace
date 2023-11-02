from django.contrib import admin

# Local imports
from .models import Shipment, Location
from core.admin import BaseAdmin


@admin.register(Shipment)
class ShipmentAdmin(BaseAdmin):
    """
    This class is used to register Shipment model in django admin panel
    """

    list_display = ("tracking_number", "article_name")


@admin.register(Location)
class LocationAdmin(BaseAdmin):
    """
    This class is used to register Location model in django admin panel
    """

    list_display = ("country_name", "city_name", "zip_code")