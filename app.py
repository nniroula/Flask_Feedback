from flask import Flask, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from forms import UserForm, LoginForm


app = Flask(__name__)


# for flask debugtoolbar setup need secret key and a html file
app.config["SECRET_KEY"] = "flaskDebugToolbarRequiresSecretKey"
debug = DebugToolbarExtension(app)

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

#for SQLAlchemy configuration
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///flask_feedback_db'
app.config['AQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

# for models.py
connect_db(app)
db.drop_all()
db.create_all()
@app.route('/')
def home_page():
    # return render_template("base.html") 
    return redirect('/register')

@app.route('/register')
def show_registration_form():
    form = UserForm()
    return render_template("register.html", form = form)

@app.route("/secret")
def secret():
    return "You made it"

@app.route('/register', methods = ["POST"])
def process_registration():
    form = UserForm()
    if 'username' in session:
        return redirect(f"/users/{session['username']}")
    if form.validate_on_submit():
        unam = form.username.data   # username comes from forms.py
        pword = form.password.data
        emal = form.email.data
        fname = form.first_name.data    # first_name comes from a Form class in forms.py
        lname = form.last_name.data
        
        # new_user = User.register(username = unam, password = pword, email = emal, first_name = fname, last_name = lname)
        new_user = User.register(unam, pword, emal, fname, lname)
        
        db.session.add(new_user)
        db.session.commit()

        return redirect('/secret')

# GET /login
# Show a form that when submitted will login a user. This form should accept a username and a password.
@app.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if 'username' in session:
        return redirect(f"/users/{session['username']}")

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        existing_user = User.authenticate(username, password)
        if existing_user:
            return redirect('/secret')
    return render_template('login.html', form = form)

"""
Part 2: Make a Base Template
Add a base template with slots for the page title and content. Your other templates should use this.

You can use Bootstrap for this project, but don’t spend a lot of time worrying about styling — this is not a goal of this exercise.
"""

"""
Part 3: Make Routes For Users
Make routes for the following:

GET /
Redirect to /register.
GET /register
Show a form that when submitted will register/create a user. This form should accept a username, password, email, first_name, and last_name.

Make sure you are using WTForms and that your password input hides the characters that the user is typing!

POST /register
Process the registration form by adding a new user. Then redirect to /secret
GET /login
Show a form that when submitted will login a user. This form should accept a username and a password.

Make sure you are using WTForms and that your password input hides the characters that the user is typing!

POST /login
Process the login form, ensuring the user is authenticated and going to /secret if so.
GET /secret
Return the text “You made it!” (don’t worry, we’ll get rid of this soon)

"""
