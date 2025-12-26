import os
from celery import Celery


# set default django settings module for 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app.settings')

app = Celery('alx_travel_app')

# Load config from django settings, namespace 'CELERY' means
# all celery-related config keys should start with 'CELERY_'
app.config_from_object('django.conf:settings', namespace='CELERY')

# load task modules from all registered django apps
app.autodiscover_tasks()
