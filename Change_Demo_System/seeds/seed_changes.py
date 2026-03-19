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

    change3 = Change(
        short_description="Replace Firewall Hardware",
        business_justification="End-of-life hardware requires replacement to maintain security compliance.",
        risk="Major",
        approver=infrastructure_team_approver.id,
        assigned_to=infrastructure_team_user.id,
        assignment_group=infrastructure_team_group.id,
        state="Scheduled",
    )

    change4 = Change(
        short_description="Deploy New Email Filtering Rules",
        business_justification="Reduces phishing attempts and improves email security.",
        risk="Minor",
        approver=service_desk_approver.id,
        assigned_to=service_desk_user.id,
        assignment_group=service_desk_group.id,
        state="New",
    )

    change5 = Change(
        short_description="Patch Linux Servers",
        business_justification="Critical security patches released by vendor.",
        risk="Moderate",
        approver=infrastructure_team_approver.id,
        assigned_to=infrastructure_team_user.id,
        assignment_group=infrastructure_team_group.id,
        state="Implement",
        start_date_time=datetime(2026, 4, 2, 1, 0)
    )

    change6 = Change(
        short_description="Upgrade CRM Application",
        business_justification="Vendor upgrade required for continued support.",
        risk="Major",
        approver=application_support_approver.id,
        assigned_to=application_support_user.id,
        assignment_group=application_support_group.id,
        state="Closed",
        start_date_time=datetime(2026, 2, 10, 22, 0),
        end_date_time=datetime(2026, 2, 11, 2, 30)
    )

    change7 = Change(
        short_description="Network Switch Firmware Update",
        business_justification="Fixes known stability issues affecting branch offices.",
        risk="Minor",
        approver=infrastructure_team_approver.id,
        assigned_to=infrastructure_team_user.id,
        assignment_group=infrastructure_team_group.id,
        state="Approved",
        start_date_time=datetime(2026, 5, 1, 3, 0),
    )

    change8 = Change(
        short_description="Add New User Provisioning Workflow",
        business_justification="Improves onboarding efficiency and reduces manual work.",
        risk="Moderate",
        approver=request_team_approver.id,
        assigned_to=request_team_user.id,
        assignment_group=request_team_group.id,
        state="Closed",
        start_date_time=datetime(2026, 1, 20, 9, 0),
        end_date_time=datetime(2026, 1, 20, 11, 45)
    )

    change9 = Change(
        short_description="Migrate File Shares to Cloud Storage",
        business_justification="Reduces on-prem storage costs and increases availability.",
        risk="Major",
        approver=service_desk_approver.id,
        assigned_to=service_desk_user.id,
        assignment_group=service_desk_group.id,
        state="Implement",
        start_date_time=datetime(2026, 3, 28, 14, 0),
    )

    change10 = Change(
        short_description="Install Security Agent on Endpoints",
        business_justification="Required for compliance with new security policy.",
        risk="Low",
        approver=request_team_approver.id,
        assigned_to=request_team_user.id,
        assignment_group=request_team_group.id,
        state="Closed",
        start_date_time=datetime(2026, 3, 5, 8, 30),
        end_date_time=datetime(2026, 3, 5, 9, 15)
    )

    db.session.add_all([change1, change2, change3, change4,change5,change6,change7,change8,change9,change10])
    db.session.commit()