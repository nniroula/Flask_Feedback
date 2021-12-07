from flask_sqlalchemy import SQLAlchemy
from flask_wtf.form import FlaskForm
import sqlalchemy
from flask_bcrypt import Bcrypt
from wtforms.fields.simple import PasswordField, StringField
from wtforms.validators import InputRequired

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

bcrypt = Bcrypt()

class User(db.Model):
    __tablename__ = "users"
    username = db.Column(db.String(20), primary_key = True, unique = True)
    password = db.Column(db.Text, nullable = False)
    email = db.Column(db.String(50), unique =  True, nullable = False)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False) 

    # define a method to register a user
    @classmethod
    def register(cls, username, password, email, first_name, last_name):
        # register a user with hashed password
        hashed = bcrypt.generate_password_hash(password)
        # now turn byte string into a normal unicode utf8 string
        hashed_utf8 = hashed.decode("utf8")
        # return the instance of user with username and hashed password
        user = cls(username = username, password = hashed_utf8, email = email, first_name = first_name, last_name = last_name )
        return user # user is an instance of the model class

    @classmethod
    def authenticate(cls, username, pword):
        u = User.query.filter_by(username = username).first()
        if u and bcrypt.check_password_hash(u.password, pword):
            return u
        else:
            False
        

"""
Part 1: Create User Model
First, create a User model for SQLAlchemy. Put this in a models.py file.

It should have the following columns:

username - a unique primary key that is no longer than 20 characters.
password - a not-nullable column that is text
email - a not-nullable column that is unique and no longer than 50 characters.
first_name - a not-nullable column that is no longer than 30 characters.
last_name - a not-nullable column that is no longer than 30 characters.

"""