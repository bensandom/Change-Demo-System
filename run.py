from Change_Demo_System import create_app
from Change_Demo_System.extensions import db
from Change_Demo_System.models import User, Change, Group, UserGroup

app = create_app()

with app.app_context():
    db.create_all()

    if User.query.count() == 0:
        from Change_Demo_System.seeds.seed_users import seed_users
        seed_users()
        

    if Group.query.count() == 0:
        from Change_Demo_System.seeds.seed_groups import seed_groups
        seed_groups()

    if UserGroup.query.count() == 0:
        from Change_Demo_System.seeds.seed_usergroups import seed_usergroups
        seed_usergroups()
    
    if Change.query.count() == 0:
        from Change_Demo_System.seeds.seed_changes import seed_changes
        seed_changes()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)