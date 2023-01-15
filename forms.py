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
    password = PasswordField("Password", validators = [DataRequired()])
    submit_button = SubmitField()

class UserProfileForm(FlaskForm):
    display_name = StringField('Display Name', validators = [DataRequired()])
    profession = StringField('Profession', validators = [DataRequired()])
    phone_number = StringField('Phone Number', validators = [DataRequired()])
    location = StringField('Location', validators = [DataRequired()])
    hobbies = StringField('Hobbies', validators = [DataRequired()])
    submit_button = SubmitField()


# class AddBookForm(FlaskForm):
    # id = StringField('ID', validators=[DataRequired()])
    # book_id = StringField('Book ID', validators=[DataRequired()])
    # user_token = StringField('User Token', validators=[DataRequired()], default=lambda: current_user.token)