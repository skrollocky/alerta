import os
from celery import Celery,shared_task
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "back.settings")
app = Celery("back")
app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()



@shared_task
def checker():
    print("Xui")