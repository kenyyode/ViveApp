from flask_wtf import FlaskForm
from Vive import app
from wtforms import StringField, IntegerField, EmailField, SelectField, PasswordField, SubmitField, FloatField
from wtforms.validators import InputRequired, Length, ValidationError, EqualTo
from models import User, BodyMass
from flask import flash


class Registration(FlaskForm):
    username = StringField(label='Username', validators=[InputRequired(),Length(min=4, max=20)],
                                                   render_kw={'placeholder':'username'})
    name = StringField("Name", validators=[InputRequired()],
                       render_kw={"placeholder":"John Doe"})
    age = IntegerField("Age", validators=[InputRequired()],
                       render_kw={'placeholder':'Age'})
    email = EmailField("Email", validators=[InputRequired()],
                       render_kw={"placeholder":"johndoe@gmail.com"})
    sex = SelectField("Gender", choices=[("male", "Male"), ("female", "Female")], validators=[InputRequired()])
    phonenumber = StringField("Phone Number", validators=[InputRequired()],
                               render_kw={'placeholder':"+234 000 000"})
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=16)])
    
    submit = SubmitField("Sign Up")
    
    ## now the validation 
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username Already Taken")
        
class Login_form(FlaskForm):
    username= StringField("Username", validators=[InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder":"username"})
    password = PasswordField("Password", validators=[InputRequired(), Length(min=4, max=20)],
                             render_kw={'placeholder':'password'})
    submit = SubmitField("Login")
    
class forgot_password(FlaskForm):
    username= StringField("Username", validators=[InputRequired(), Length(min=4, max=20)],
                           render_kw={"placeholder":"username"})
    new_password = PasswordField("New Password", validators=[InputRequired(), Length(min=8, max=20)],
                                 render_kw={"placeholder":"New Password"})
    confirm_password = PasswordField("Confirm Password", validators=[InputRequired(), Length(min=8, max=20)],
                                 render_kw={"placeholder":"Confirm Password"})
    submit = SubmitField("Change Password")
    
    def validate(self):
        if not super().validate():
            return False

        if self.new_password.data != self.confirm_password.data:
            flash("Passwords do not match", "error")
            return False

        return True
    
class bodymass(FlaskForm):
        height = FloatField(validators=[InputRequired()], 
                            render_kw={"placeholder":"Height in cm"})
        weight = FloatField(
            validators=[InputRequired()],
            render_kw = {"placeholder":"Weight in kg"}
        )
        
        submit = SubmitField("Save")