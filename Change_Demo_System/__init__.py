import os
from flask import Flask
from .extensions import db, login_manager
from Change_Demo_System.models import User

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secret"
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    login_manager.init_app(app)
    ## Importing Database models after the app has been intialised
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
## REgistering all blueprints for routes so they can be used later
    from .routes.auth import auth_bp
    from .routes.changes import change_bp
    from .routes.user_management import user_management_bp
    from .routes.group_management import group_bp
    from .routes.usergroup_management import usergroup_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(change_bp)
    app.register_blueprint(user_management_bp)
    app.register_blueprint(group_bp)
    app.register_blueprint(usergroup_bp)

    ## Creating tables and adding static seeds
    with app.app_context():
        db.create_all()
        from Change_Demo_System.models import Group, UserGroup, Change

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

    return app
