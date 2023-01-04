
import eventlet
eventlet.monkey_patch(all=False, socket=True)

from application.webserver import WebServer
from application.messagequeue import MessageQueue

from flask import Flask
from flask_socketio import SocketIO

celery = eventlet.import_patched("celery")


message_queue = MessageQueue().message_queue
webserver = WebServer()
app = Flask(__name__)
cel = celery.Celery(broker=message_queue)
socketio = SocketIO(app, message_queue=message_queue)

import application.views
import application.events
