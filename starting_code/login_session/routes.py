from werkzeug.utils import redirect
from flask_login import login_user, logout_user
from . import app, db, bcrypt
from flask import render_template, request, url_for
from .models import User

@app.route('/')
def home():

        return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        #Get data from the form
        username = request.form["username"]
        password = request.form["password"]

        #Check if user exists
        user = User.query.filter_by(username=username).first()
        if user:
            return render_template('register.html', message='Username already exists')

        #Encrypt password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        #Add user to db
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        #Get data from the form
        username = request.form["username"]
        password = request.form["password"]

        #Check if user exists
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            # session["username"] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', message="Invalid username or password")

    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    # session.pop('username', None)
    return redirect(url_for('home'))
