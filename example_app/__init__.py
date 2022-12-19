
import eventlet
eventlet.monkey_patch()

import socket

import redis
from flask import Flask
from flask_socketio import SocketIO
from celery import Celery

if redis.Redis().ping():
    pass
else:
    raise Exception("You need redis: https://redis.io/docs/getting-started/installation/. Check that redis-server.service is running!")

ip = "127.0.0.1"
port = 8080
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    s.connect(("1.1.1.1", 1))
    ip = s.getsockname()[0]
finally:
    s.close()

app = Flask(__name__)
app.config["MESSAGE_BROKER"] = "redis://localhost:6379/0"

socketio = SocketIO(app, message_queue=app.config["MESSAGE_BROKER"])

cel = Celery(__name__, broker=app.config["MESSAGE_BROKER"], include=["example_app.tasks"])
cel.conf.update(app.config)

from . import views
from . import events

socketio.run(app, host=ip, port=port, use_reloader=False, debug=True)