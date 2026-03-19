from Change_Demo_System import db
from Change_Demo_System.models import User, Group, UserGroup
from tests.factories import create_group, edit_group, delete_group

##Database Testing
## Tests creating a group
def test_create_group(app):

    group = create_group(name="Test Group 2")
    assert Group.query.filter_by(name="Test Group 2").first() is not None

## Tests editing a group
def test_edit_group(app):
    
    group = create_group(name="Test Group 5")
    edited_group = edit_group(group, name="Edited Group 5")
    assert edited_group.name == "Edited Group 5"

## Tests deleting a group
def test_delete_group(app):
    
    group = create_group(name="Test Group 6")
    delete_group(group)
    assert Group.query.filter_by(name="Test Group 6").first() is None

##Route Testing
## Tests the group list route - has to be logged in to do this
def route_test_group_list(app, logged_in_client):
    # Create a group
    group = create_group(name="Test Group 1")

    response = logged_in_client.get("/groups")

    assert response.status_code == 200
    assert b"Test Group 1" in response.data

## Tests the group create route - has to be logged in to do this
def route_test_create_group(app, logged_in_client):
    response = logged_in_client.post("/groups/create", data={
        "name": "Test Group 2"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Test Group 2" in response.data

## Tests the group edit route - has to be logged in to do this
def route_test_edit_group(app, logged_in_client):
    
    group = create_group(name="Test Group 3")
    response = logged_in_client.post(f"/groups/edit/{group.id}", data={
        "name": "Edited Group 3"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Edited Group 3" in response.data

## Tests the group delete route - has to be logged in to do this
def route_test_delete_group(app, logged_in_client):
    
    group = create_group(name="Test Group 4")
    response = logged_in_client.post(f"/groups/delete/{group.id}", follow_redirects=True)

    assert response.status_code == 200
    assert b"Test Group 4" not in response.data