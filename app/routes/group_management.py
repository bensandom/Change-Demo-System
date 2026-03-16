from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from ..models import User, Group, UserGroup
from ..extensions import db

group_bp = Blueprint('group_management', __name__)

@group_bp.route("/group_list", methods=["GET"])
@login_required
def group_list():
    groups = Group.query.all()
    return render_template("group_management/group_list.html", groups=groups)

@group_bp.route("/view_group/<int:group_id>", methods=["GET"])
@login_required
def view_group(group_id):
    group = Group.query.get(group_id)
    return render_template("group_management/view_group.html", group=group)

@group_bp.route("/add_group", methods=["GET", "POST"])
@login_required
def add_group():
    if request.method == "POST":
        name = request.form["name"]

        new_group = Group(name=name)
        db.session.add(new_group)
        db.session.commit()

        return redirect(url_for("group_management.group_list"))

    return render_template("group_management/add_group.html")

@group_bp.route("/edit_group/<int:group_id>", methods=["GET", "POST"])
@login_required
def edit_group(group_id):
    group = Group.query.get(group_id)
    if request.method == "POST":
        group.name = request.form["name"]
        db.session.commit()
        return redirect(url_for("group_management.group_list"))

    return render_template("group_management/edit_group.html", group=group)

@group_bp.route("/delete_group/<int:group_id>", methods=["POST"])
@login_required
def delete_group(group_id):
    group = Group.query.get(group_id)
    db.session.delete(group)
    db.session.commit()
    return redirect(url_for("group_management.group_list"))

