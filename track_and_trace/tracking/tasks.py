from datetime import datetime, timedelta
from django.utils import timezone

from celery import shared_task
from tracking.weather_service import get_weather_data


@shared_task
def weather_data_retrieval(hours: int = 2):
    """
    Retrieves weather data for locations
    that are not modified for the given hours

    Args:
        hours (int): number of hours to update weather
            default = 2
    """

    from .models import Location

    all_locations = Location.objects.all()

    for location in all_locations:
        # Get seconds of time delta from now and last update
        timedelta_seconds = (timezone.now() - location.last_updated).total_seconds()

        if timedelta_seconds > (3600 * hours):
            weather_data = get_weather_data(location.city_name)["weather"][0]["description"]
            location.weather = weather_data
            location.save()
            print(f"{location.country_name}, {location.city_name} updated! > {weather_data}")


@shared_task
def sample_task():
    print("The sample task just ran.")
