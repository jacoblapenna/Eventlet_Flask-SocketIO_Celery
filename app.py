# needed to use redis
import eventlet
eventlet.monkey_patch()

# needed to emit from another process
import redis

# data stream and control object
from data import Data

from flask import Flask, render_template
from flask_socketio import SocketIO

# create app and Socket.IO server objects
app = Flask(__name__)
socketio = SocketIO(app, message_queue='redis://')

# serve page
@app.route('/')
def index():
    return render_template("index.html")

# listen for and handle data stream request
@socketio.on("start_data")
def start_data():
    data = Data()
    data.run()


# run app
if __name__ == "__main__":

    # make sure redis-server.service is running
    if redis.Redis().ping():
        pass
    else:
        raise Exception("You need redis: https://redis.io/docs/getting-started/installation/. Check that redis-server.service is running!")

    # specify server LAN address
    ip = "192.168.1.8" # insert server ip here as needed
    port = 8080

    # run application
    socketio.run(app, host=ip, port=port, use_reloader=False, debug=True)