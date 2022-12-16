from multiprocessing import Process
from random import randrange
import time

from celery import Celery
from flask_socketio import SocketIO

class Data:

    def __init__(self, broker):
        self._socketio = SocketIO(message_queue=broker)
        self._cel = Celery(broker=broker)
        # self._worker = self._cel.Worker(self.)

    def _stream(self):

        @self._cel.task
        def data_emit(websocket, event, data):
            websocket.emit(event, data=data)
            return 0

        while True:
            value = randrange(0, 1000, 1) / 100
            data_emit.delay(self._socketio.emit, "new_data", {"value" :  value})
    
    def run(self):
        process = Process(target=self._stream, name="data_stream")
        process.start()
