from flask import Flask
from celery import Celery

app = Flask(__name__)
app.config["MESSAGE_BROKER"] = "redis://localhost:6379/0"
cel = Celery(__name__, broker=app.config["MESSAGE_BROKER"], include=["example_app.tasks"])
cel.conf.update(app.config)

import example_app.views