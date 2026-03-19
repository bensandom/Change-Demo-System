from Change_Demo_System import db
from Change_Demo_System.models import User, Group, UserGroup
from tests.factories import create_user, create_group, add_user_to_group, remove_user_from_group

## Database testing 

## Tests adding a user to a group
def test_add_user_to_group(app):
    # Create a user and a group
    user = create_user(username="Test User 4", password="password", role="User")
    group = create_group(name="Test Group 4")

    # Add the user to the group
    user_group = add_user_to_group(user, group)

    assert UserGroup.query.filter_by(user_id=user.id, group_id=group.id).first() is not None

## Tests removing a user from a group
def test_remove_user_from_group(app):
    # Create a user and a group
    user = create_user(username="Test User 5", password="password", role="User")
    group = create_group(name="Test Group 5")

    # Add the user to the group
    add_user_to_group(user, group)

    # Remove the user from the group
    remove_user_from_group(user, group)

    assert UserGroup.query.filter_by(user_id=user.id, group_id=group.id).first() is None

## Route testing
## Tests adding a user to a group - has to be logged in to do this
def route_test_add_user_to_group(app, logged_in_client):
    # Create a user and a group
    user = create_user(username="Test User 7", password="password", role="User")
    group = create_group(name="Test Group 7")

    # Check Group is created
    response = logged_in_client.post(
        "/usergroup/add",
        data={"user_id": user.id, "group_id": group.id},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Test Group 7" in response.data


## Tests removing a user from a group - has to be logged in to do this
def route_test_remove_user_from_group(app, logged_in_client):
    # Create a user and a group
    user = create_user(username="Test User 8", password="password", role="User")
    group = create_group(name="Test Group 8")

    # Add the user to the group
    add_user_to_group(user, group)

    # Check Group is removed
    response = logged_in_client.post(
        "/usergroup/remove",
        data={"user_id": user.id, "group_id": group.id},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Test Group 8" not in response.data

