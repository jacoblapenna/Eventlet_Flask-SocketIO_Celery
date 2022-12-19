from flask import Flask

app = Flask(__name__)
app.config["MESSAGE_BROKER"] = "redis://localhost:6379/0"

import app.app