
from application import socketio, message_queue
from application.tasks import stream_data

from flask import request

@socketio.on("start_data_stream")
def start_data_stream():
    stream_data.delay(request.sid, message_queue)