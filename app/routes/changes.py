from flask import Blueprint, render_template, url_for, request, redirect
from flask_login import login_required
from ..models import Change, User, Group
from ..extensions import db
from datetime import datetime

change_bp = Blueprint('change', __name__)

##Lists All Changes - Requires Login
@change_bp.route("/change_list", methods=["GET"])
@login_required
def change_list():
    changes = Change.query.all()
    return render_template("change_list.html", changes=changes)

## Add New Change - Requires Login
@change_bp.route("/add_change", methods=["GET","POST"])
@login_required
def add_change():
    if request.method == "POST":
        short_description = request.form["short_description"]
        business_justification = request.form["business_justification"]
        risk = request.form["risk"]
        approver_id = request.form["approver"]
        assigned_to_id = request.form["assigned_to"]
        assignment_group_id = request.form["assignment_group"]

        new_change = Change(
            short_description=short_description,
            business_justification=business_justification,
            risk=risk,
            approver=approver_id,
            assigned_to=assigned_to_id,
            assignment_group = assignment_group_id
        )
        db.session.add(new_change)
        db.session.commit()
        return redirect(url_for("change.change_list"))

    risk_options = ["Minor", "Moderate", "Major"]
    all_users = User.query.all()
    approvers = User.query.filter_by(role="Admin").all()
    groups = Group.query.all()
    return render_template("add_change.html", approvers=approvers, risk_options=risk_options, groups=groups, all_users=all_users)

##View Change Details - Requires Login
@change_bp.route("/change/<int:change_id>/view", methods=["GET"])
@login_required
def view_change(change_id):
    change = Change.query.get(change_id)
    return render_template("view_change.html", change=change)

##Edit an Existing Change - Requires Login
@change_bp.route("/change/<int:change_id>/edit", methods=["GET", "POST"])
@login_required
def edit_change(change_id):
    change = Change.query.get(change_id)
    users = User.query.all()
    groups = Group.query.all()

    if request.method == "POST":
        change.short_description = request.form["short_description"]
        change.business_justification = request.form["business_justification"]
        change.risk = request.form["risk"]
        change.approver = request.form["approver"]
        db.session.commit()
        return redirect(url_for("change.change_list"))

    return render_template("edit_change.html", change=change, users=users, groups=groups)

## Delete a Change - Requires Login
@change_bp.route("/change/<int:change_id>/delete", methods=["GET","POST"])
@login_required
def delete_change(change_id):
    change = Change.query.get(change_id)
    db.session.delete(change)
    db.session.commit()
    return redirect(url_for("change.change_list"))

##Approve a Change - Requires Login
@change_bp.route("/change/<int:change_id>/approve", methods=["GET","POST"])
@login_required
def approve_change(change_id):
    change = Change.query.get(change_id)
    change.state = "Scheduled"
    db.session.commit()

    return redirect(url_for("change.view_change", change_id=change.id))

## Reject a Change - Requires Login
@change_bp.route("/change/<int:change_id>/reject", methods=["GET","POST"])
@login_required
def reject_change(change_id):
    change = Change.query.get(change_id)
    change.state = "New"
    db.session.commit()
    return redirect(url_for("change.view_change", change_id=change.id))

## Implements a change - Requires Login
@change_bp.route("/change/<int:change_id>/implement", methods=["GET","POST"])
@login_required
def implement_change(change_id):
    change = Change.query.get(change_id)
    change.start_date_time = datetime.now()
    change.state = "Implemented"
    db.session.commit()

    return redirect(url_for("change.view_change", change_id=change.id))

## Complete a change - Requires Login
@change_bp.route("/change/<int:change_id>/complete", methods=["GET","POST"])
@login_required
def complete_change(change_id):
    change = Change.query.get(change_id)
    change.end_date_time = datetime.now()
    change.state = "Completed"
    db.session.commit()

    return redirect(url_for("change.view_change", change_id=change.id))

## Send For Approval - Requires Login
@change_bp.route("/change/<int:change_id>/send_for_approval", methods=["GET", "POST"])
@login_required
def send_for_approval(change_id):
    change = Change.query.get(change_id)
    change.state = "Authorise"
    db.session.commit()

    return redirect(url_for("change.view_change", change_id=change.id))


