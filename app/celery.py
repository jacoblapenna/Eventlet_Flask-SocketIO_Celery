from celery import Celery
from app import app

cel = Celery("app", broker=app["MESSAGE_BROKER"], include=app.tasks)

if __name__ == "__main__":
    cel.start()