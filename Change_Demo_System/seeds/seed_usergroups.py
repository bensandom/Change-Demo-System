from Change_Demo_System.extensions import db
from Change_Demo_System.models import User, Group, UserGroup

def seed_usergroups():
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

    db.session.add_all([
    # Admin belongs to all groups
    UserGroup(user_id=default_admin.id, group_id=service_desk_group.id),
    UserGroup(user_id=default_admin.id, group_id=request_team_group.id),
    UserGroup(user_id=default_admin.id, group_id=infrastructure_team_group.id),
    UserGroup(user_id=default_admin.id, group_id=application_support_group.id),

    # Default user belongs to Service Desk
    UserGroup(user_id=default_user.id, group_id=service_desk_group.id),

    # Service Desk team
    UserGroup(user_id=service_desk_approver.id, group_id=service_desk_group.id),
    UserGroup(user_id=service_desk_user.id, group_id=service_desk_group.id),

    # Request Team
    UserGroup(user_id=request_team_approver.id, group_id=request_team_group.id),
    UserGroup(user_id=request_team_user.id, group_id=request_team_group.id),

    # Infrastructure Team
    UserGroup(user_id=infrastructure_team_approver.id, group_id=infrastructure_team_group.id),
    UserGroup(user_id=infrastructure_team_user.id, group_id=infrastructure_team_group.id),

    # Application Support
    UserGroup(user_id=application_support_approver.id, group_id=application_support_group.id),
    UserGroup(user_id=application_support_user.id, group_id=application_support_group.id),

    # Change Manager belongs to all groups
    UserGroup(user_id=change_manager.id, group_id=service_desk_group.id),
    UserGroup(user_id=change_manager.id, group_id=request_team_group.id),
    UserGroup(user_id=change_manager.id, group_id=infrastructure_team_group.id),
    UserGroup(user_id=change_manager.id, group_id=application_support_group.id)])
    db.session.commit()