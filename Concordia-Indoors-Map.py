__author__ = 'jaspreet'

# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash

# create our application
app = Flask(__name__)
app.config.from_envvar('MAPS_SETTINGS', silent=True) #MAPS_SETTINGS is a environ var where we store the location of config file
#MAPS_SETTINGS envr var can be set as export MAPS_SETTINGS=/flaskr/settings.cfg. See Readme.
#used to connect to DB and return connection.
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

# fires up the server if we want to run that file as a standalone application
if __name__ == '__main__':
    app.run()
