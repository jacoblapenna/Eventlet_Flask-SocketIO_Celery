
from application import message_queue

import eventlet
celery = eventlet.import_patched("celery")


cel = celery.Celery(broker=message_queue, backend=message_queue)