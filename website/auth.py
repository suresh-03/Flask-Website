from flask import Blueprint, flash, render_template, request

auth = Blueprint("auth", __name__)


@auth.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")
        confirmPass = request.form.get("confpass")

        if len(password) < 8:
            flash("password must be more than 8 Characters!", category="error")
        elif password != confirmPass:
            flash("re-confirm the password!", category="error")
        else:
            flash("Account created!", category="success")

    return render_template("signup.html")


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/logout")
def logout():
    return render_template("login.html")
