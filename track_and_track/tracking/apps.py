from django.apps import AppConfig
from django.db.models.signals import post_save


class TrackingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "tracking"

    def ready(self):
        from . import signals