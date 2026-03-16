from app.extensions import db
from app.models import User

def seed_users():
    service_desk_approver = User(username="service_desk_approver", password="service_desk_approver", role="Admin")
    service_desk_user = User(username="service_desk_user", password="service_desk_user", role="User")
    request_team_approver = User(username="request_approver", password="request_approver", role="Admin")
    request_team_user = User(username="request_user", password="request_user", role="User")
    infrastructure_team_approver = User(username="infrastructure_approver", password="infrastructure_approver", role="Admin")
    infrastructure_team_user = User(username="infrastructure_user", password="infrastructure_user", role="User")
    application_support_approver = User(username="application_support_approver", password="application_support_approver", role="Admin")
    application_support_user = User(username="application_support_user", password="application_support_user", role="User")
    default_admin = User(username="admin", password="admin", role="Admin")
    change_manager = User(username="Change_Manager", password="change_manager", role="Admin")
    default_user = User(username="user", password="user", role="User")

    db.session.add_all([service_desk_approver, service_desk_user, request_team_approver, request_team_user, infrastructure_team_approver, infrastructure_team_user, application_support_approver, application_support_user, default_admin, change_manager, default_user])
    db.session.commit()