from Change_Demo_System.extensions import db
from Change_Demo_System.models import Group

def seed_groups():
    Service_Desk_Group = Group(name="Service Desk")
    Request_Team_Group = Group(name="Request Team")
    Infrastructure_Team_Group = Group(name="Infrastructure Team")
    Application_Support_Group = Group(name="Application Support Team")
    db.session.add_all([Service_Desk_Group, Request_Team_Group, Infrastructure_Team_Group, Application_Support_Group])
    db.session.commit()