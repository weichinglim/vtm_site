import pytest
from app import app as flask_app

#this is setup file - pre setup a value to go look for

@pytest.fixture()
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()
