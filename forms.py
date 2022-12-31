from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

# Sign-up form
class UserSignupForm(FlaskForm):
    first = StringField('First Name', validators = [DataRequired()])
    last = StringField('Last Name', validators = [DataRequired()])
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

class UserLoginForm(FlaskForm):
    email = StringField("Email", validators = [DataRequired()])
    password = StringField("Password", validators = [DataRequired()])
    submit_button = SubmitField()

class UserProfileForm(FlaskForm):
    nickname = StringField('Nickname')
    