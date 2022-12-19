
from . import socketio

socketio.run(app, host=ip, port=port, use_reloader=False, debug=True)