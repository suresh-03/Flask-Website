from flask import Blueprint, flash, render_template, request, redirect, url_for
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User

auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        confirmPass = request.form.get("confpass")

        if len(password) < 6:
            flash("password must be more than 8 Characters!", category="error")
        elif password != confirmPass:
            flash("re-confirm the password!", category="error")
        else:
            new_user = User(
                name=name,
                email=email,
                password=generate_password_hash(password, method="sha256"),
            )
            db.session.add(new_user)
            db.session.commit()
            flash("Account created!", category="success")
            return redirect(url_for("views.home"))

    return render_template("signup.html")


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return render_template("login.html")
