from django.urls import path

# Local imports
from . import views


app_name = "tracking"


urlpatterns = [
    path("shipments/", views.ShipmentView.as_view(), name="shipment-list"),
]
