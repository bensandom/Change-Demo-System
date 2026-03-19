from Change_Demo_System import db
from Change_Demo_System.models import User, Group, UserGroup
from tests.factories import create_user, create_group, add_user_to_group

## Testing logging in with a new user
def test_login_success(app, client):
    # Create a user
    user = create_user(username="testuser", password="password", role="User")
    ## Logsin with that user
    response = client.post("/login", data={
        "username": "testuser",
        "password": "password"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Logout" in response.data

##Test logging in with wrong password
def test_login_failure(app, client):
    from Change_Demo_System.models import User
    from Change_Demo_System.extensions import db
    ## Create a user
    user = create_user(username="testuser", password="password",role="User")
    ## Attempt to log in with wrong password
    response = client.post("/login", data={
        "username": "testuser",
        "password": "wrongpassword"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Login" in response.data

## Testing logging out
def test_logout(app, logged_in_client):
    response = logged_in_client.get("/logout", follow_redirects=True)

    assert response.status_code == 200
    assert b"Login" in response.data

## Testing registering a new user
def test_register(app, client):
    response = client.post("/register", data={
        "username": "newuser",
        "password": "newpassword"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Login" in response.data

##Testing registering a user with an existing username
def test_register_existing_user(app, client):
    # Create a user
    user = create_user(username="testuser", password="password", role="User")

    # Attempt to register with the same username
    response = client.post("/register", data={
        "username": "testuser",
        "password": "newpassword"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Username already exists" in response.data