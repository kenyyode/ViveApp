from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
csrf = CSRFProtect(app)
db= SQLAlchemy(app)
app.config["SECRET_KEY"] = "mysecretkey"
bcrypt = Bcrypt(app)