import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# https://realpython.com/flask-by-example-part-1-project-setup/

app = Flask(__name__)

try:
    APP_SETTINGS = os.environ['APP_SETTINGS']
except:
    APP_SETTINGS = "config.DevelopmentConfig"
app.config.from_object(APP_SETTINGS)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Result

@app.route('/')
def hello():
    return "Hello World!"


@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()