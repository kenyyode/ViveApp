from Vive import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True) # unique identifier
    name = db.Column(db.String(20), nullable=False, unique=False)
    username = db.Column(db.String(20), nullable=False, unique=True)
    age = db.Column(db.Integer(), nullable=False, unique=False)
    email = db.Column(db.String(), nullable=False)
    sex = db.Column(db.String(), nullable=False, unique=False)
    password = db.Column(db.String(80), nullable=False, unique=False)
    phonenumber = db.Column(db.String(), nullable=False, unique=False)
    
    def __repr__(self):
        return f"<User {self.username}>"