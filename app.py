
import eventlet
eventlet.monkey_patch()

from random import randrange

import redis

from flask import Flask, render_template
from flask_socketio import SocketIO

from make_celery import make_celery
from celery import Celery


app = Flask(__name__)
message_broker = "redis://localhost:6379/0"
app.config.update(CELERY_BROKER_URL = message_broker, CELERY_RESULT_BACKEND=message_broker)

socketio = SocketIO(app, message_queue=message_broker)

cel = make_celery(app)

# serve page
@app.route('/')
def index():
    return render_template("index.html")

@socketio.on("start_data_stream")
def start_data_stream():

    print("Starting data stream...")
    result = stream_data.delay()

    print(result)

@cel.task
def stream_data():

    data_socketio = SocketIO(message_queue=message_broker)
    print("Streaming data...")
    i = 1

    while i <= 100000:
        value = randrange(0, 1000, 1) / 100
        data_socketio.emit("new_data", {"value" :  value})
        i += 1


if __name__ == "__main__":

    if redis.Redis().ping():
        pass
    else:
        raise Exception("You need redis: https://redis.io/docs/getting-started/installation/. Check that redis-server.service is running!")

    ip = "192.168.1.8"
    port = 8080

    socketio.run(app, host=ip, port=port, use_reloader=False, debug=True)
