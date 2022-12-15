from multiprocessing import Process
from random import randrange
import time

from flask_socketio import SocketIO

class Data:

    def __init__(self):
        self._socketio = SocketIO(message_queue='redis://')

    def _stream(self):
        while True:
            value = randrange(0, 1000, 1) / 100
            self._socketio.emit("new_data", data={"value" :  value})
            time.sleep(0.1)
    
    def run(self):
        process = Process(target=self._stream, name="data_stream")
        process.start()