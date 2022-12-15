import eventlet
eventlet.monkey_patch()

import redis

from data import Data

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, message_queue='redis://')
socketio.init_app(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template("index.html")

@socketio.on("start_data")
def start_data():
    data = Data()
    data.run()
    print("Button pressed")

if __name__ == "__main__":

    # make sure redis-server.service is running
    if redis.Redis().ping():
        pass
    else:
        raise Exception("Check that redis-server.service is running!")

    # specify server LAN address
    ip = "192.168.1.8"
    port = 8080

    # run application
    socketio.run(app, host=ip, port=port, use_reloader=False, debug=True)