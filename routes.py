from Vive import app, db, bcrypt
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, LoginManager, logout_user
from forms import Registration, Login_form, forgot_password
from models import User
from wtforms.validators import ValidationError 

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
            else: 
                flash("Incorrect Credentials")
        else: 
            flash("User does not exist")
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

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect (url_for("Login"))

@app.route ("/Forgot_Password", methods=["POST", "GET"])
def Forgot_Password():
    form = forgot_password()
    if form.validate():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user:
            hashed_password = bcrypt.generate_password_hash(form.new_password.data)
            user.password = User(password=hashed_password)
        
        try:
            db.sesson.commit()
            flash("Password Changed Succesfully")
        except:
            ValidationError ("Validation Error")
        return redirect("/Login")
    return render_template ("forgot.html", form=form)
