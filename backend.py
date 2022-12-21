
from random import randrange

import redis

from flask import Flask, render_template
from flask_socketio import SocketIO
from celery import Celery


message_broker = "redis://localhost:6379/0"

app = Flask(__name__)
socketio = SocketIO(app)

cel = Celery("backend", broker=message_broker, backend=message_broker)

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on("start_data_stream")
def start_data_stream():

    print("Starting data stream...")
    result = stream_data.delay(100, 100)
    
    s = result.state
    last_s = None
    monitor = True

    while monitor:
        
        if s != last_s:
            print(s)
        elif s == "FAILURE" or s == "SUCCESS":
            monitor = False

        last_s = s
        s = result.state

    print(f"Task returned with status {s} and result {result.result}")

@cel.task()
def stream_data(a, b):

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
