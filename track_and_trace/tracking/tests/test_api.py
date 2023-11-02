import json
import pytest
from django.urls import reverse
from django.test import Client
from tracking.models import Shipment

pytestmark = pytest.mark.django_db
shipments_url = reverse("tracking:shipment-list")


# ===================== Test Get Shipments ====================== #
def test_zero_shipments(client: Client) -> None:
    """
    Test zero shipments should return empty list
    """

    response = client.get(shipments_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


def test_get_shipment_with_tracking_number(
    client: Client, shipments: list[Shipment]
) -> None:
    """
    Test that get shipment with tracking number
    should return shipment data
    """

    response = client.get(
        shipments_url, {"tracking_number": shipments[0].tracking_number}
    )
    first_shipment_data = json.loads(response.content)[0]

    assert (
        first_shipment_data["tracking_number"] == shipments[0].tracking_number
    )


def test_get_shipment_with_carrier(
    client: Client, shipments: list[Shipment]
) -> None:
    """
    Test that get shipment with carrier
    should return shipment data
    """

    response = client.get(shipments_url, {"carrier": shipments[0].carrier})
    first_shipment_data = json.loads(response.content)[0]

    assert first_shipment_data["carrier"] == shipments[0].carrier


def test_get_shipments_with_same_tracking_number(
    client: Client, shipments: list[Shipment]
) -> None:
    """
    Test Get shipments with same tracking number
    """

    response = client.get(
        shipments_url, {"tracking_number": shipments[0].tracking_number}
    )
    shipments_data = json.loads(response.content)

    # First and second have same tracking number
    assert shipments[0].tracking_number == shipments[1].tracking_number
    assert len(shipments_data) == 2


def test_get_shipment_with_no_query_param(
    client: Client, shipments: list[Shipment]
) -> None:
    """
    Test that get shipment with no query params to filter
    should return empty list
    """

    response = client.get(shipments_url, {})

    shipment_data = json.loads(response.content)
    assert shipment_data == []
    assert shipments[0] not in shipment_data
