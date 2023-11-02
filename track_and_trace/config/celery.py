import os
import logging
from celery import Celery
from django.conf import settings


logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery(
    'backend',
)
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()