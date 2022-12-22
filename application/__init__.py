
import eventlet
eventlet.monkey_patch(all=False, socket=True)

from application.webserver import WebServer
from application.messagequeue import MessageQueue

from flask import Flask
from flask_socketio import SocketIO


message_queue = MessageQueue().message_queue
webserver = WebServer()
app = Flask(__name__)
socketio = SocketIO(app, message_queue=message_queue)

import application.views
import application.events
import application.celery