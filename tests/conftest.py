import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from Change_Demo_System import create_app, User
from Change_Demo_System.extensions import db

@pytest.fixture
def app():
    app = create_app()

    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
        "WTF_CSRF_ENABLED": False,
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def logged_in_client(app):
    client = app.test_client()

    # Create User
    user = User(username="testuser", password="password")
    db.session.add(user)
    db.session.commit()

    # Log in
    response = client.post(
        "/login",
        data={"username": "testuser", "password": "password"},
        follow_redirects=True
    )

    # Check if login was successful
    assert response.status_code == 200

    return client
