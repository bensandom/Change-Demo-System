from Change_Demo_System.extensions import db
from Change_Demo_System.models import User

def seed_users():
    User.query.delete()
    db.session.commit()
    service_desk_approver = User(username="sd_approver", password="sd_approver", role="Admin")
    service_desk_user = User(username="sd_user", password="sd_user", role="User")
    request_team_approver = User(username="req_approver", password="req_approver", role="Admin")
    request_team_user = User(username="req_user", password="req_user", role="User")
    infrastructure_team_approver = User(username="inf_approver", password="inf_approver", role="Admin")
    infrastructure_team_user = User(username="inf_user", password="inf_user", role="User")
    application_support_approver = User(username="app_sup_approver", password="app_sup_approver", role="Admin")
    application_support_user = User(username="app_sup_user", password="app_sup_user", role="User")
    default_admin = User(username="admin", password="admin", role="Admin")
    change_manager = User(username="Change_Manager", password="change_manager", role="Admin")
    default_user = User(username="user", password="user", role="User")

    db.session.add_all([service_desk_approver, service_desk_user, request_team_approver, request_team_user, infrastructure_team_approver, infrastructure_team_user, application_support_approver, application_support_user, default_admin, change_manager, default_user])
    db.session.commit()
