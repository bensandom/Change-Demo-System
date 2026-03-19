from Change_Demo_System import db
from Change_Demo_System.models import User, Group, UserGroup,Change

## User Functions
## Function to call to create a user
def create_user(username, password, role):
    user = User(username=username, role=role, password=password)
    db.session.add(user)
    db.session.commit()
    return user

##Function to call to edit a user
def edit_user(user, username, password, role):
    user.username = username
    user.password = password
    user.role = role
    db.session.commit()
    return user

## Function to call to delete a user
def delete_user(user):
    db.session.delete(user)
    db.session.commit()


## Group Functions
## Function to call to create a group
def create_group(name):
    group = Group(name=name)
    db.session.add(group)
    db.session.commit()
    return group

## Function to call to edit a group
def edit_group(group, name):
    group.name = name
    db.session.commit()
    return group

## Function to call to delete a group
def delete_group(group):
    db.session.delete(group)
    db.session.commit()

## UserGroup Functions
## Function to call to add a user to a group
def add_user_to_group(user, group):
    user_group = UserGroup(user_id=user.id, group_id=group.id)
    db.session.add(user_group)
    db.session.commit()
    return user_group

## Function to call to remove a user from a group
def remove_user_from_group(user, group):
    user_group = UserGroup.query.filter_by(user_id=user.id, group_id=group.id).first()
    if user_group:
        db.session.delete(user_group)
        db.session.commit()

## Change Functions
##Function to call to create a change
def create_change(short_description, business_justification, risk, approver, assigned_to, assignment_group):
    change = Change(short_description=short_description, business_justification=business_justification, risk=risk, approver=approver, assigned_to=assigned_to, assignment_group=assignment_group)
    db.session.add(change)
    db.session.commit()
    return change

## Function to call to edit a change
def edit_change(change, short_description, business_justification, risk, approver, assigned_to, assignment_group, state, start_date_time, end_date_time):
    change.short_description = short_description
    change.business_justification = business_justification
    change.risk = risk
    change.approver = approver
    change.assigned_to = assigned_to
    change.assignment_group = assignment_group
    change.state = state
    change.start_date_time = start_date_time
    change.end_date_time = end_date_time
    db.session.commit()
    return change

## Function to call to delete a change
def delete_change(change):
    db.session.delete(change)
    db.session.commit()