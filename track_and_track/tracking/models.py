from django.db import models
from django.utils.translation import gettext_lazy as _

# local imports
from core.models import BaseModel


class StatusOptions(models.TextChoices):
    """
    This class used as status choices
    """

    SCANNED = "scanned", _("scanned")
    IN_TRANSIT = "in-transit", _("in-transit")
    DELIVERY = "delivery", _("delivery")
    TRANSIT = "transit", _("transit")
    INBOUND_SCAN = "inbound-scan", _("inbound-scan")


class Location(BaseModel):
    """This class used to represent the address"""

    line1 = models.CharField(max_length=100, verbose_name=_("line 1"))
    city_name = models.CharField(max_length=100, verbose_name=_("city name"),
                                 unique=True)
    country_name = models.CharField(
        max_length=100, verbose_name=_("country name")
    )
    zip_code = models.IntegerField(verbose_name=_("zip code"), unique=True)
    weather = models.CharField(max_length=150, verbose_name=_("weather"))

    class Meta:
        verbose_name = _("location")
        verbose_name_plural = _("locations")

    def __str__(self):
        return f"{self.line1}, {self.zip_code} {self.city_name}, {self.country_name}"

    @classmethod
    def from_address(cls, address: str) -> "Location":
        """
        Constructs a Location object
        from parsed address string

        Args:
            address(str): address to parse location from it
                Sample: "Street 1, 10115 Berlin, Germany"
        Return:
            Location: new location object
        """

        splitted_address = [item.strip() for item in address.split(",")]

        line1 = splitted_address[0]
        zip_code, city_name = splitted_address[1].split(" ")
        country_name = splitted_address[2]

        location, _ = Location.objects.get_or_create(
            line1=line1,
            zip_code=zip_code,
            city_name=city_name,
            country_name=country_name,
        )
        return location
