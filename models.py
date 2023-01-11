from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid 
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask_login import LoginManager
from flask_marshmallow import Marshmallow 
import secrets

# Set variables for class instantiation
login_manager = LoginManager()
ma = Marshmallow()
db = SQLAlchemy()

@login_manager.user_loader
def load_user(user_token):
    return User.query.get(user_token)


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    first = db.Column(db.String(150), nullable = True, default='')
    last = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default = '', unique = True )
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __init__(self, email, first='', last='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.first = first
        self.last = last
        self.password = self.set_password(password)
        self.email = email
        self.token = self.set_token(24)
        self.g_auth_verify = g_auth_verify

    def set_token(self, length):
        return secrets.token_hex(length)

    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'User {self.email} has been added to the database'


class Profile(db.Model):
    id = db.Column(db.String, primary_key = True)
    display_name = db.Column(db.String, nullable = False)
    profession = db.Column(db.String, nullable = False)
    phone_number = db.Column(db.String, nullable = False)
    location = db.Column(db.String, nullable = False)
    hobbies = db.Column(db.String, nullable = False)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, display_name, profession, phone_number, location, hobbies, user_token, id = ''):
        self.id = self.set_id()
        self.display_name = display_name
        self.profession = profession
        self.phone_number = phone_number
        self.location = location
        self.hobbies = hobbies
        self.user_token = user_token

    def set_id(self):
        return (secrets.token_urlsafe())


class ProfileSchema(ma.Schema):
    class Meta:
        fields = ['display_name', 'profession', 'phone_number', 'location', 'hobbies']


profile_schema = ProfileSchema()
profile_schemas = ProfileSchema(many = True)

class UserBooks(db.Model):
    id = db.Column(db.String, primary_key = True)
    book_id = db.column(db.String, nullable = False)
    user_token = db.column(db.String, db.ForeignKey('user.token'), nullable = False)
    
    def __init__(self, book_id, user_token, id = ''):
        self.id = self.set_id()
        self.book_id = book_id
        self.user_token = user_token

    def set_id(self):
        return (secrets.token_urlsafe())

