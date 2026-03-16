from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from ..models import User
from ..extensions import db

session_management_bp = Blueprint('session_management', __name__)

@session_management_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            return redirect(url_for("change.change_list"))
        return render_template("log_in.html", error="Invalid username or password")
    return render_template("log_in.html")

@session_management_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user:
            return render_template("register.html", error="Username already exists")

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for("session_management.login"))

    return render_template("register.html")

@session_management_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("session_management.login"))