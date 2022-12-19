
from celery import Celery

def make_celery(app):

    cel = Celery(app.import_name, broker=app.config["CELERY_BROKER_URL"])
    cel.conf.update(app.config)

    class ContextTask(cel.Task):

        abstract = True

        def __call__(self, *args, **kwargs):

            with app.app_context():
                return self.run(*args, **kwargs)
    
    cel.Task = ContextTask
    
    return cel