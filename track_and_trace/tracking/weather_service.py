import requests
from django.conf import settings


def get_weather_data(city_name) -> dict:
    """
    Get weather data by city name from openweather API
    :param city_name: the city to get its weather data
    :return: dict of weather data
    """
    api_key: str = settings.OPEN_WEATHER_API_KEY
    url: str = (
        f"https://api.openweathermap.org/data/2.5/weather?q="
        f"{city_name}&appid={api_key}"
    )

    response = requests.get(url)
    return response.json()
