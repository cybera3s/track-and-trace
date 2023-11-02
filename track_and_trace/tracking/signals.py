from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Location
from .weather_service import get_weather_data


@receiver(post_save, sender=Location)
def fetch_weather(sender, instance, **kwargs):
    """
    Fetches weather data on create
    """

    if kwargs["created"]:
        weather_data: dict = get_weather_data(instance.city_name)
        instance.weather = weather_data["weather"][0]["description"]
        instance.save()