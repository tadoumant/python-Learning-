from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from pythonic.models import User

class RegistrationForm(FlaskForm):
    fname = StringField(
        "First Name", validators=[DataRequired(), Length(min=2, max=25)]
    )
    lname = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=25)])
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=25)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Regexp(
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$"
            ),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    #validation Username
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already Exists')
        
    #validation Email
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already Exists')

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
        ],
    )
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")

"""
from tokenize import String
# first pip install flask-wtf
from flask_wtf import FlaskForm
#inport StringField
from wtforms import StringField,PasswordField,SubmitField,BooleanField
#import dataRequired (ex assister de remplire une forme ) ||  [Regexp:import Regular Expressions] ||[EqualTo = check his equal to other form]
from wtforms.validators import DataRequired,Length,Email,Regexp,EqualTo #import Email validator (avant pip install email_validator)

class RegistrationForm(FlaskForm):
    fname = StringField("First Name",Validators=[DataRequired(),Length(min=2,max=25)])#Validators:check input validation ex Length =(min=2 chara max=10 chara)
    lname = StringField("Last Name",Validators=[DataRequired(),Length(min=2,max=25)])
    username = StringField("Username",Validators=[DataRequired(),Length(min=2,max=25)])
    email = StringField("Email",Validators=[DataRequired(),Email()])#/  ,Regexp("'^(=.*[a-z])(?=.*[A-Z])(?=.*\d)(?.*[@$!%*?&_])[A-Za-z\d@$!%*?&_]{8,32}$'")   #/
    password = PasswordField("Password",Validators=[DataRequired()])#min =8 char max=10char uppermin:1 lowermin:1 numbermin : 1 specielchara min:1
    confirm_password = PasswordField("Confirm Password",Validators=[DataRequired,EqualTo("password")])
    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = StringField("Email",Validators=[DataRequired(),Email()])
    password = PasswordField("Password",Validators=[DataRequired()])
    remember=BooleanField("Remember Me")
    submit = SubmitField("Sign Up")
"""