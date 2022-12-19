from celery import Celery
from example_app import app

cel = Celery("app", broker=app["MESSAGE_BROKER"], include=example_app.tasks)

if __name__ == "__main__":
    cel.start()