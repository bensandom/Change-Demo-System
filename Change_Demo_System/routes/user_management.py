from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from ..models import User, Group, UserGroup
from ..extensions import db

## Allows us to group related routes together and import them into the main app
user_management_bp = Blueprint('user_management', __name__)

## Gets a list of all users - Requires Login
@user_management_bp.route("/user_list", methods=["GET"])
@login_required
def user_list():
    users = User.query.all()
    return render_template("user_list.html", users=users)

## Gets details for a specific user - Requires Login
@user_management_bp.route("/view_user/<int:user_id>", methods=["GET"])
@login_required
def view_user(user_id):
    user = User.query.get(user_id)
    return render_template("view_user.html", user=user)

## Adds a new user to the system - Requires Login
@user_management_bp.route("/add_user", methods=["GET", "POST"])
@login_required
def add_user():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]
        ## If the username already exists, show an error. Otherwise, create the new user and add it to the database
        if User.query.filter_by(username=username).first():
            return render_template("add_user.html", error="Username already exists")
        else:
            new_user = User(username=username, password=password, role=role)
            db.session.add(new_user)
            db.session.commit()

        return redirect(url_for("user_management.user_list"))
    ## Need to pass the role options to the template to populate the dropdown in the form
    role_options = ["Admin", "User"]
    return render_template("add_user.html", role_options=role_options)

## Edits an existing user - Requires Login
@user_management_bp.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
@login_required
def edit_user(user_id):
    ## Need to get the user being edited, the role options for the dropdown and the list of all groups to populate the group assignment section of the form
    user = User.query.get(user_id)
    role_options = ["Admin", "User"]
    all_groups = Group.query.all()
    user_group_ids = [g.id for g in user.groups]
    if request.method == "POST":
        user.username = request.form["username"]
        user.role = request.form["role"]
        db.session.commit()
        return redirect(url_for("user_management.user_list"))

    return render_template("edit_user.html", user=user, role_options=role_options, all_groups=all_groups, user_group_ids=user_group_ids)

## Deletes a user from the system - Requires Login
@user_management_bp.route("/delete_user/<int:user_id>", methods=["GET", "POST"])
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("user_management.user_list"))


