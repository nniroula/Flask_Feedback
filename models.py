from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class User(db.Model):
    __tablename__ = "users"
    username = db.Column(db.String(20), primary_key = True, unique = True)
    password = db.Column(db.Text, nullable = False)
    email = db.Column(db.String(50), unique =  True, nullable = False)
    first_name = db.Column(db.String(30), nullable = False)
    last_name = db.Column(db.String(30), nullable = False) 


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