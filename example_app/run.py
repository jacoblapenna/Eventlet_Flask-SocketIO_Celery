
from . import app, socketio, ip, port

socketio.run(app, host=ip, port=port, use_reloader=False, debug=True)