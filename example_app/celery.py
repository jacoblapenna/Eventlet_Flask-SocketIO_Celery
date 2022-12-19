from celery import Celery
from example_app import app

cel = Celery("example_app", broker=app.config["MESSAGE_BROKER"], include=["example_app.tasks"])

if __name__ == "__main__":
    cel.start()