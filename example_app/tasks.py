
from random import randrange

from . import cel
from . import app

from flask_socketio import SocketIO

@cel.task
def stream_data():

    data_socketio = SocketIO(message_queue=app.config["MESSAGE_BROKER"])
    print("Streaming data...")

    while True:
            value = randrange(0, 1000, 1) / 100
            data_socketio.emit("new_data", {"value" :  value})
