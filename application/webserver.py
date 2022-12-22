
import socket

class WebServer:

    def __init__(self, ip="127.0.0.1", port=8080):

        self.ip = ip
        self.port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        try:
            self._socket.connect(("1.1.1.1", 1))
            self.ip = self._socket.getsockname()[0]
        finally:
            self._socket.close()