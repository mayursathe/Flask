from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user_data.db"
app.secret_key = 'secret-key'
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

global COOKIE_TIME_OUT
COOKIE_TIME_OUT = 60*60*24*7 #7 days