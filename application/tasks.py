
from random import randrange
from time import sleep

from application import cel

from flask_socketio import SocketIO

@cel.task()
def stream_data(sid, message_queue):

    data_socketio = SocketIO(message_queue=message_queue)
    i = 1

    while i <= 100:
        value = randrange(0, 10000, 1) / 100
        data_socketio.emit("new_data", {"value" :  value})
        i += 1
        sleep(0.01)
