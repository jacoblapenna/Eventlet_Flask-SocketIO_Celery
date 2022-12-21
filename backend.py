
import eventlet
eventlet.monkey_patch()

from random import randrange

import redis

from flask import Flask, render_template
from flask_socketio import SocketIO

from celery import Celery


app = Flask(__name__)
message_broker = "redis://localhost:6379/0"
app.config.update(CELERY_CONFIG={'broker_url': message_broker, 'result_backend': message_broker})

socketio = SocketIO(app, message_queue=message_broker)

cel = cel = Celery(__name__)
cel.conf.update(app.config["CELERY_CONFIG"])

# serve page
@app.route('/')
def index():
    return render_template("index.html")

@socketio.on("start_data_stream")
def start_data_stream():

    print("Starting data stream...")
    result = stream_data.delay()
    s = result.status
    last_s = None

    while s != "FAILURE" or s != "SUCCESS":
        if s != last_s:
            print(s)
        last_s = s
        s = result.status
    
    print(s, result.result)

@cel.task()
def stream_data():

    data_socketio = SocketIO(message_queue=message_broker)
    i = 1

    while i <= 100:
        value = randrange(0, 1000, 1) / 100
        data_socketio.emit("new_data", {"value" :  value})
        i += 1
    
    return i, value


if __name__ == "__main__":

    if redis.Redis().ping():
        pass
    else:
        raise Exception("You need redis: https://redis.io/docs/getting-started/installation/. Check that redis-server.service is running!")

    ip = "192.168.1.8" # insert LAN address here
    port = 8080

    socketio.run(app, host=ip, port=port, use_reloader=False, debug=True)
