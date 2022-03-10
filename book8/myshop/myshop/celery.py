import os
from celery import Celery

# set the default Djano settings module for the 'celery' progra.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myshop.settings")

app = Celery("myshop", broker="amqps://biwtdill:CluzjrW2PGcyvFM-V3f6av-QYkNaRJba@goose.rmq2.cloudamqp.com/biwtdill")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()