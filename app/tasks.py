
from random import randrange

from .celery import cel
from flask_socketio import SocketIO

@cel.task
def stream_data(broker):

    data_socketio = SocketIO(message_queue=broker)

    while True:
            value = randrange(0, 1000, 1) / 100
            data_socketio.emit("new_data", {"value" :  value})

    # def __init__(self, broker):
    #     self._socketio = SocketIO(message_queue=broker)
    #     self._cel = Celery(broker=broker)
    #     # self._worker = self._cel.Worker(self.)

    # def _stream(self):

    #     @self._cel.task
    #     def data_emit(event, data):
    #         self._socketio.emit(event, data=data)

    #     while True:
    #         value = randrange(0, 1000, 1) / 100
    #         data_emit.delay("new_data", {"value" :  value})
    
    # def run(self):
    #     process = Process(target=self._stream, name="data_stream")
    #     process.start()
