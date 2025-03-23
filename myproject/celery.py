import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
redis_url = os.getenv("CELERY_BROKER_URL", "redis://redis:6379/0")

celery_app = Celery("myproject", broker=redis_url)
celery_app.config_from_object("django.conf:settings", namespace="CELERY")
celery_app.autodiscover_tasks()