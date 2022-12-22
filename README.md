This package is a basic real-time web application for streaming some CPU intensive data process from the server. It gets around eventlet and multiprocessing issues by using specific imports and monkey patching, with celery as the task manager.

1. clone
2. `cd /path/to/clone`
3. `python -m venv .env`
4. `source .env/bin/activate`
5. `pip install --upgrade pip`
6. `pip install -r `