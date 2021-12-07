from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.simple import PasswordField, StringField
from wtforms.validators import InputRequired

class UserForm(FlaskForm):
    username = StringField("user name")
    password = PasswordField("password")
    email = StringField("Email")
    first_name = StringField("First Name")
    last_name = StringField("Last Name")

class LoginForm(FlaskForm):
    __tablename__ = "user_login"
    username = StringField("username", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired()])

"""
Show a form that when submitted will register/create a user. This form should accept a username, password, email, first_name, and last_name.

Make sure you are using WTForms and that your password input hides the characters that the user is typing!
"""