__author__ = 'jaspreet'

import os, sys, logging
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from flask import Flask, request, render_template,redirect,url_for, flash
from flask.ext.login import LoginManager, login_required

app = Flask(__name__)

SECRET_KEY = "WHY IS THIS 'SECRET KEY' THING NECESSARY I DONT GET IT!?"

app.config.from_object(__name__)

@app.route("/")
def hello():
    return render_template("main.html",helloworldmsg="hello world!")

if __name__ == "__main__":
    app.run(debug=True)