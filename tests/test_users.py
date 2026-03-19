from Change_Demo_System import db
from Change_Demo_System.models import User, Group, UserGroup
from tests.factories import create_user, create_group, add_user_to_group, remove_user_from_group, edit_user, delete_user

##Database Testing
## Tests creating a user
def test_create_user(app):

    user = create_user(username="Test User 2", password="password", role="User")
    assert User.query.filter_by(username="Test User 2").first() is not None

## Tests editing a user
def test_edit_user(app):
    
    user = create_user(username="Test User 5", password="password", role="User")
    edited_user = edit_user(user, username="Edited User 5", password="newpassword", role="Admin")
    assert edited_user.username == "Edited User 5"
    assert edited_user.password == "newpassword"
    assert edited_user.role == "Admin"

## Tests deleting a user
def test_delete_user(app):
    
    user = create_user(username="Test User 6", password="password", role="User")
    delete_user(user)
    assert User.query.filter_by(username="Test User 6").first() is None




##Route Testing

## Tests the user list route - has to be logged to do this
def route_test_user_list(app, logged_in_client):
    # Create a user
    user = create_user(username="Test User 1", password="password", role="User")

    response = logged_in_client.get("/users")

    assert response.status_code == 200
    assert b"Test User 1" in response.data

## Tests the user create route - has to be logged in to do this
def route_test_create_user(app, logged_in_client):
    response = logged_in_client.post("/users/create", data={
        "username": "Test User 2",
        "password": "password",
        "role": "User"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Test User 2" in response.data

## Tests the user edit route - has to be logged in to do this
def route_test_edit_user(app, logged_in_client):
    
    user = create_user(username="Test User 3", password="password", role="User")
    response = logged_in_client.post(f"/users/edit/{user.id}", data={
        "username": "Edited User 3",
        "password": "newpassword",
        "role": "Admin"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Edited User 3" in response.data

## Tests the user delete route - has to be logged in to do this
def route_test_delete_user(app, logged_in_client):
    
    user = create_user(username="Test User 4", password="password", role="User")
    response = logged_in_client.post(f"/users/delete/{user.id}", follow_redirects=True)

    assert response.status_code == 200
    assert b"Test User 4" not in response.data

