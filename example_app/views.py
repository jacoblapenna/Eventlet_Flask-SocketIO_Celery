
from . import app

from flask import render_template


# serve page
@app.route('/')
def index():
    return render_template("index.html")
