from celery import Celery
import os

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

app = Celery(
    "markposition",
    broker=redis_url,
    backend=redis_url,
    include=["markposition.tasks"]
)

app.conf.update(
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    timezone="UTC",
    enable_utc=True,
)

if __name__ == "__main__":
    app.start()
