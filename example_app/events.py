
from . import app, socketio
from .tasks import stream_data

# listen for and handle data stream request
@socketio.on("start_data_stream")
def start_data_stream():

    stream_data.delay(app.config["MESSAGE_BROKER"])