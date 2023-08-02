from Vive import app, db, bcrypt
from flask import Flask, render_template, redirect, url_for, request
from flask_login import login_user, login_required, LoginManager
from forms import Registration, Login_form
from models import User

login_manager= LoginManager()
login_manager.init_app(app) # this initializes the app called app
login_manager.login_view = "Login" #this creates an endpoint for when an unathorized user tries to access a restricted page

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/", methods=["POST", "GET"])
def index():
    return redirect ("/Login")

@app.route("/Login", methods=["GET", "POST"])
def Login():
    form = Login_form()
    if form.validate_on_submit():
        user= User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect ("/dashboard")
    return render_template ("login.html", form=form)

@app.route ("/registration", methods=["POST", "GET"])
def registration():
    form = Registration()
    if form.validate_on_submit():
        hashed_password= bcrypt.generate_password_hash(form.password.data)
        new_user=User(username=form.username.data, password=hashed_password, 
                  name=form.name.data, age=form.age.data, sex=form.sex.data, email=form.email.data,
                  phonenumber=form.phonenumber.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect ("/dashboard")
    return render_template("register.html", form=form)

@app.route("/dashboard", methods = ["POST", "GET"])
@login_required
def dashboard():
    return render_template("dashboard.html")