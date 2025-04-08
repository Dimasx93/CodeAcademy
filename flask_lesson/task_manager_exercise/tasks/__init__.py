from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app: Flask = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI']: str = 'sqlite:///tasks.db'
db: SQLAlchemy = SQLAlchemy(app)


from .routes import *