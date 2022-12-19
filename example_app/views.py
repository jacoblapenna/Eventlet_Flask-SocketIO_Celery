# needed to use redis
import eventlet
eventlet.monkey_patch()

# from gevent import monkey
# monkey.patch_all()

# needed to emit from another process
import redis


from example_app import app
from example_app.tasks import stream_data

from flask import render_template
from flask_socketio import SocketIO

# create app and Socket.IO server objects
socketio = SocketIO(app, message_queue=app.config["MESSAGE_BROKER"], async_mode="eventlet")

# serve page
@app.route('/')
def index():
    return render_template("index.html")

# listen for and handle data stream request
@socketio.on("start_data")
def start_data():

    stream_data.delay(app.config["MESSAGE_BROKER"])

    """  THIS BREAKS WEBSOCKETS WHEN PROCESS IS RAN FROM HERE """
    """ COMMENT/UNCOMMENT BELOW """
    # data = Data(app.config["MESSAGE_BROKER"])
    # data.run()
    """ COMMENT/UNCOMMENT ABOVE """

    # pass
    


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

    """ THIS WORKS WHEN PROCESS IS RAN FROM HERE """
    """ COMMENT/UNCOMMENT BELOW """
    # data = Data()
    # data.run()
    """ COMMENT/UNCOMMENT ABOVE """

    # run application
    socketio.run(app, host=ip, port=port, use_reloader=False, debug=True)