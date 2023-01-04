
import subprocess

from application import app, socketio, webserver
from redis import Redis


# check redis service and flush old messages
r = Redis()

if r.ping():
    pass
else:
    raise Exception("You need redis: https://redis.io/docs/getting-started/installation/. Check that redis-server.service is running!")

r.flushall()


# start celery worker
cmd = "celery -A application.cel worker".split(' ')
subprocess.Popen(cmd)


# run the app
socketio.run(app, host=webserver.ip, port=webserver.port, use_reloader=False, debug=True)