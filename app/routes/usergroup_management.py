from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from ..models import User, Group, UserGroup
from ..extensions import db

usergroup_bp = Blueprint('usergroup_management', __name__)

@usergroup_bp.route("/usergroup/<int:user_id>/<int:group_id>/add", methods=["POST"])
@login_required
def add_user_to_group(user_id, group_id):
    user_group = UserGroup(user_id=user_id, group_id=group_id)
    db.session.add(user_group)
    db.session.commit()
    return redirect(url_for("user_management.view_user", user_id=user_id))

@usergroup_bp.route("/usergroup/<int:user_id>/<int:group_id>/remove", methods=["GET","POST"])
@login_required
def remove_user_from_group(user_id, group_id):
    user_group = UserGroup.query.filter_by(user_id=user_id, group_id=group_id).first()
    if user_group:
        db.session.delete(user_group)
        db.session.commit()
    return redirect(url_for("user_management.view_user", user_id=user_id))