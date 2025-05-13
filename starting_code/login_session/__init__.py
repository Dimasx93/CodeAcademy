from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'secret_key'  # Change this to a secure secret key

app.config['SQLALCHEMY_DATABASE_URI']: str = 'sqlite:///login.db'
db: SQLAlchemy = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'home'

bcrypt = Bcrypt(app)

from .routes import *