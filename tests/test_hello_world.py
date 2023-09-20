import pytest
from tests.test_hello_world import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_hello_world(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b'Hello, World!' in response.data