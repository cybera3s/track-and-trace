import os
import logging
from celery import Celery


logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery(
    "backend",
)
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
