from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from ..models import User, Group, UserGroup
from ..extensions import db

## Allows us to group related routes together and import them into the main app
usergroup_bp = Blueprint('usergroup_management', __name__)

## Creates a new association between a user and a group - Requires Login
@usergroup_bp.route("/usergroup/add", methods=["GET", "POST"])
@login_required
def add_user_to_group():
    if request.method == "POST":
        user_id = request.form["user_id"]
        group_id = request.form["group_id"]
        ## Check if the association already exists. If not, create it and add it to the database
        if UserGroup.query.filter_by(user_id=user_id, group_id=group_id).first():
            return render_template("add_user_to_group.html", users=User.query.all(), groups=Group.query.all(), error="User is already in this group")
        else:
            new_user_group = UserGroup(user_id=user_id, group_id=group_id)
            db.session.add(new_user_group)
            db.session.commit()
        return redirect(url_for("user_management.view_user", user_id=user_id))
    
    return render_template("add_user_to_group.html", users=User.query.all(), groups=Group.query.all())

## Removes the usergroup record - Requires Login
@usergroup_bp.route("/usergroup/<int:user_id>/<int:group_id>/remove", methods=["GET","POST"])
@login_required
def remove_user_from_group(user_id, group_id):
    user_group = UserGroup.query.filter_by(user_id=user_id, group_id=group_id).first()
    if user_group:
        db.session.delete(user_group)
        db.session.commit()
    return redirect(url_for("user_management.view_user", user_id=user_id))