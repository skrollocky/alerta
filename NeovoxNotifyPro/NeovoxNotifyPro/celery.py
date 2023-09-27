import os
from celery import Celery
from celery.schedules import crontab



os.environ.setdefault("DJANGO_SETTINGS_MODULE", '<name_of_project>.settings')

app = Celery('<name_of_project>')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()



# заносим таски в очередь
app.conf.beat_schedule = {
    'every': { 
        'task': '<name_of_app>.tasks.repeat_order_make',
        'schedule': crontab(),# по умолчанию выполняет каждую минуту, очень гибко 
    },                                                              # настраивается

}
