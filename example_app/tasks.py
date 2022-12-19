
from random import randrange

from . import cel

from flask_socketio import SocketIO

@cel.task
def stream_data(broker):

    data_socketio = SocketIO(message_queue=broker)

    while True:
            value = randrange(0, 1000, 1) / 100
            data_socketio.emit("new_data", {"value" :  value})
