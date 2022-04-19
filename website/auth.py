from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import check_password_hash, generate_password_hash
from website import db
from flask_login import login_required, login_user, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash(f"Logged in successfully, welcome {user.first_name}", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.index'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')


    return render_template("login.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route("/sign-up", methods=["POST", "GET"])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password = request.form.get('password1')
        confirm_password = request.form.get('password2')  


        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already taken, try again', category='error')
        elif len(firstname) < 2:
            flash('Name should be greater than 1 character', category='error')
        elif len(password) < 6:
            flash('Password should be greater than 6 characters', category='error')
        elif password != confirm_password:
            flash('Passwords do not match, try again', category='error')
        else:
            new_user = User(email=email, first_name=firstname, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            flash('Account created!', category='success') 
            return redirect(url_for('views.index'))  

    return render_template("sign_up.html")


