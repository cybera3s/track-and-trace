import pytest
from typing import List
from tracking.models import Shipment, Location, StatusOptions
from django.db.models import signals


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture
def location1() -> Location:
    # Disable signals
    signals.post_save.receivers = []

    return Location.objects.create(
        line1="line 1",
        city_name="test city",
        country_name="test country",
        zip_code="123456",
        weather="",
    )


@pytest.fixture
def location2() -> Location:
    # Disable signals
    signals.post_save.receivers = []

    return Location.objects.create(
        line1="line 2",
        city_name="test2 city",
        country_name="test2 country",
        zip_code="654321",
        weather="",
    )


@pytest.fixture
def shipment1(location1, location2) -> Shipment:
    return Shipment.objects.create(
        tracking_number="123456",
        carrier="abc",
        sender_address=location1,
        receiver_address=location2,
        article_name="Shipment1",
        article_quantity=1,
        article_price=123,
        sku="sku1",
        status=StatusOptions.IN_TRANSIT
    )


@pytest.fixture
def shipment2(location1, location2) -> Shipment:
    return Shipment.objects.create(
        tracking_number="123456",
        carrier="abc",
        sender_address=location1,
        receiver_address=location2,
        article_name="Shipment2",
        article_quantity=3,
        article_price=321,
        sku="sku2",
        status=StatusOptions.IN_TRANSIT
    )


@pytest.fixture
def shipment3(location1, location2) -> Shipment:
    return Shipment.objects.create(
        tracking_number="987654",
        carrier="cba",
        sender_address=location2,
        receiver_address=location1,
        article_name="Shipment3",
        article_quantity=5,
        article_price=6543,
        sku="sku3",
        status=StatusOptions.DELIVERY,
    )


@pytest.fixture
def shipments(shipment1, shipment2, shipment3) -> List[Shipment]:
    return [shipment1, shipment2, shipment3]
