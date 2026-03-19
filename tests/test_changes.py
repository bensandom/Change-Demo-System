from Change_Demo_System import db
from Change_Demo_System.models import Change, User, Group, UserGroup
from tests.factories import create_change, edit_change, delete_change
from datetime import datetime

## Database Testing

## Tests creating a change
def test_create_change(app):
    change =create_change(short_description="Test Change 1", risk="Minor", business_justification="Testing", approver=1, assigned_to=1, assignment_group=1)
    assert Change.query.filter_by(short_description="Test Change 1").first() is not None

## Tests editing a change
def test_edit_change(app):
    change = create_change(short_description="Test Change 2", risk="Minor", business_justification="Testing", approver=1, assigned_to=1, assignment_group=1)
    edited_change = edit_change(change, short_description="Edited Change 2", risk="Major", business_justification="Edited Testing", approver=2, assigned_to=2, assignment_group=2, state="Closed", start_date_time=datetime(2023, 1, 1, 0, 0, 0), end_date_time=datetime(2023, 1, 1, 1, 0, 0))
    assert edited_change.short_description == "Edited Change 2"
    assert edited_change.risk == "Major"
    assert edited_change.business_justification == "Edited Testing"
    assert edited_change.approver == 2
    assert edited_change.assigned_to == 2
    assert edited_change.assignment_group == 2
    assert edited_change.state == "Closed"
    assert str(edited_change.start_date_time) == datetime(2023, 1, 1, 0, 0, 0).strftime("%Y-%m-%d %H:%M:%S")
    assert str(edited_change.end_date_time) == datetime(2023, 1, 1, 1, 0, 0).strftime("%Y-%m-%d %H:%M:%S")

## Tests deleting a change
def test_delete_change(app):
    change = create_change(short_description="Test Change 3", risk="Minor", business_justification="Testing", approver=1, assigned_to=1, assignment_group=1)
    delete_change(change)
    assert Change.query.filter_by(short_description="Test Change 3").first() is None

##Route Testing
## Tests the change list route - has to be logged in to do this
def route_test_change_list(app, logged_in_client):
    # Create a change
    change = create_change(short_description="Test Change 4", risk="Minor", business_justification="Testing", approver=1, assigned_to=1, assignment_group=1)

    response = logged_in_client.get("/changes")

    assert response.status_code == 200
    assert b"Test Change 4" in response.data

## Tests the change create route - has to be logged in to do this
def route_test_create_change(app, logged_in_client):
    response = logged_in_client.post("/changes/create", data={
        "short_description": "Test Change 5",
        "risk": "Minor",
        "business_justification": "Testing",
        "approver": 1,
        "assigned_to": 1,
        "assignment_group": 1
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Test Change 5" in response.data

## Tests the change edit route - has to be logged in to do this
def route_test_edit_change(app, logged_in_client):
    change = create_change(short_description="Test Change 6", risk="Minor", business_justification="Testing", approver=1, assigned_to=1, assignment_group=1)
    response = logged_in_client.post(f"/changes/edit/{change.id}", data={
        "short_description": "Edited Change 6",
        "risk": "Major",
        "business_justification": "Edited Testing",
        "approver": 2,
        "assigned_to": 2,
        "assignment_group": 2,
        "state": "Closed",
        "start_date_time": datetime(2023, 1, 1, 0, 0, 0).strftime("%Y-%m-%d %H:%M:%S"),
        "end_date_time": datetime(2023, 1, 1, 1, 0, 0).strftime("%Y-%m-%d %H:%M:%S")
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Edited Change 6" in response.data
    assert b"Major" in response.data
    assert b"Edited Testing" in response.data
    assert b"2" in response.data
    assert b"Closed" in response.data
    assert b"2023-01-01 00:00:00" in response.data
    assert b"2023-01-01 01:00:00" in response.data

## Tests the change delete route - has to be logged in to do this
def route_test_delete_change(app, logged_in_client):
    change = create_change(short_description="Test Change 7", risk="Minor", business_justification="Testing", approver=1, assigned_to=1, assignment_group=1)
    response = logged_in_client.post(f"/changes/delete/{change.id}", follow_redirects=True)

    assert response.status_code == 200
    assert b"Test Change 7" not in response.data