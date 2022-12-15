from multiprocessing import Process
from random import randrange

from flask_socketio import SocketIO

class Data:

    socketio = SocketIO(message_queue='redis://')

    def __init__(self):
        pass

    def _stream(self):
        
        while True:
            value = randrange(0, 1000, 1) / 100
            self.socketio.emit("new_data", data={"value" :  value})
    
    def run(self):

        process = Process(target=self._stream, name="data_stream")
        process.start()
    
    @socketio.on("connect")
    def connect():
        print("Connection to data object!")