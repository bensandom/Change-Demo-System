from .extensions import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120), unique =True, nullable = False)
    password = db.Column(db.String(50), nullable = False)
    role = db.Column(db.String(20), nullable=False, default='User')

    groups = db.relationship('Group', secondary='user_group', backref='users')

    def __repr__(self):
        return f'<User {self.username}>'

class Change(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    short_description = db.Column(db.String(200), nullable=False)
    business_justification = db.Column(db.String(500), nullable=False)
    risk = db.Column(db.String(100), nullable=False)
    approver = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    state = db.Column(db.String(20), nullable=False, default='New')
    start_date_time = db.Column(db.DateTime, nullable=True)
    end_date_time = db.Column(db.DateTime, nullable=True)
    assignment_group = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    assigned_to = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    approver_user = db.relationship('User', foreign_keys=[approver], backref='approved_changes')
    assigned_user = db.relationship('User', foreign_keys=[assigned_to], backref='assigned_changes')
    assignment_group_rel = db.relationship('Group', backref='changes')

    def __repr__(self):
        return f'<Change {self.id}: {self.short_description}>'
    
class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    def __repr__(self):
        return f'<Group {self.name}>'

class UserGroup(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), primary_key=True)
