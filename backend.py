
import eventlet
eventlet.monkey_patch(all=False, socket=True)

from random import randrange
import time

import redis
celery = eventlet.import_patched("celery")

from flask import Flask, render_template, request
from flask_socketio import SocketIO


message_queue = "redis://localhost:6379/0"

app = Flask(__name__)
socketio = SocketIO(app, message_queue=message_queue)

cel = celery.Celery("backend", broker=message_queue, backend=message_queue)

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on("start_data_stream")
def start_data_stream():
    stream_data.delay(request.sid, message_queue)

@cel.task()
def stream_data(sid, message_queue):

    data_socketio = SocketIO(message_queue=message_queue)
    i = 1

    while i <= 100:
        value = randrange(0, 10000, 1) / 100
        data_socketio.emit("new_data", {"value" :  value})
        i += 1
        time.sleep(0.01)

    return i, value


if __name__ == "__main__":

    r = redis.Redis()
    r.flushall() # clear the old, abandoned messages from the queue

    if r.ping():
        pass
    else:
        raise Exception("You need redis: https://redis.io/docs/getting-started/installation/. Check that redis-server.service is running!")

    ip = "192.168.1.8" # insert LAN address here
    port = 8080

    socketio.run(app, host=ip, port=port, use_reloader=False, debug=True)
