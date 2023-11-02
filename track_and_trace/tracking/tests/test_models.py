from django.db.models import signals
from unittest.mock import patch, MagicMock

from tracking import weather_service
from tracking.models import Location


def test_from_address_method_of_location() -> None:
    """
    Test creating location from address should return location
    """

    # Disable signals
    signals.post_save.receivers = []

    address: str = "Daneshju 1, 123456 Mashhad, Iran"
    location = Location.from_address(address)

    assert location.line1 == "Daneshju 1"
    assert location.zip_code == "123456"
    assert location.city_name == "Mashhad"
    assert location.country_name == "Iran"
