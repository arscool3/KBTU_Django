from celery import Celery

celery_worker = Celery(
    "tasks",
    broker="amqp://guest:guest@localhost:5672/",
    backend="rpc://",
    include=["worker.tasks"]
)

celery_worker.config_from_object("worker.settings", namespace="CELERY")
