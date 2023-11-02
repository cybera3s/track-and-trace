import os
import logging
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# local imports
import tracking.tasks


logger = logging.getLogger(__name__)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")


app = Celery(
    'backend',
    namespace="CELERY_",
)

app.autodiscover_tasks()