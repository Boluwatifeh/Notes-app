import re
from flask import Blueprint, render_template, request, flash, get_flashed_messages

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=["POST", "GET"])
def login():
    
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return "<h1> Logout successful </h1>"


@auth.route("/sign-up", methods=["POST", "GET"])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password = request.form.get('password1')
        confirm_password = request.form.get('password2')  

        if len(firstname) < 2:
            flash('Name should be greater than 1 character', category='error')
        elif len(password) < 6:
            flash('Password should be greater than 6 characters', category='error')
        elif password != confirm_password:
            flash('Passwords do not match, try again', category='error')
        else:
            flash('Account created!', category='success')   

    return render_template("sign_up.html")


