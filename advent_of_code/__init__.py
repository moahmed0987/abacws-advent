from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from secret_keys import SECRET_KEY
import os

# app
app = Flask(__name__)
app.app_context().push()
app.config["SECRET_KEY"] = SECRET_KEY

# login manager
login_manager = LoginManager()
login_manager.init_app(app)

# database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "advent_of_code.db")

# initialize database
db = SQLAlchemy(app)

from advent_of_code import routes 