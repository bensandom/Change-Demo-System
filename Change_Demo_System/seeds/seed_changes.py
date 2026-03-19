from Change_Demo_System.extensions import db
from Change_Demo_System.models import User, Group, UserGroup, Change
from datetime import datetime

def seed_changes():
    service_desk_approver = User.query.filter_by(username="service_desk_approver").first()
    service_desk_user = User.query.filter_by(username="service_desk_user").first()

    request_team_approver = User.query.filter_by(username="request_approver").first()
    request_team_user = User.query.filter_by(username="request_user").first()

    infrastructure_team_approver = User.query.filter_by(username="infrastructure_approver").first()
    infrastructure_team_user = User.query.filter_by(username="infrastructure_user").first()

    application_support_approver = User.query.filter_by(username="application_support_approver").first()
    application_support_user = User.query.filter_by(username="application_support_user").first()

    default_admin = User.query.filter_by(username="admin").first()
    change_manager = User.query.filter_by(username="Change_Manager").first()
    default_user = User.query.filter_by(username="user").first()

    service_desk_group = Group.query.filter_by(name="Service Desk").first()
    request_team_group = Group.query.filter_by(name="Request Team").first()
    infrastructure_team_group = Group.query.filter_by(name="Infrastructure Team").first()
    application_support_group = Group.query.filter_by(name="Application Support Team").first()

    change1 = Change(
        short_description="Upgrade Database Server",
        business_justification="Improves performance and security.",
        risk="Major",
        approver=infrastructure_team_approver.id,
        assigned_to=infrastructure_team_user.id,
        assignment_group=infrastructure_team_group.id,
        state="Approved",

    )

    change2 = Change(
        short_description="Update Web Application",
        business_justification="Adds new features and fixes bugs.",
        risk="Moderate",
        approver=application_support_approver.id,
        assigned_to=application_support_user.id,
        assignment_group=application_support_group.id,
        state="Closed",
        start_date_time = datetime(2026, 3, 15, 10, 30),
        end_date_time = datetime(2026, 3, 15, 12, 30)
    )

    db.session.add_all([change1, change2])
    db.session.commit()