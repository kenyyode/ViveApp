from flask_wtf import FlaskForm
from Vive import app
from wtforms import StringField, IntegerField, EmailField, SelectField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from models import User


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