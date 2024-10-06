import pytest
from app import app
from db import db

@pytest.fixture
def client():
    app.config['TESTING'] = True  # Enable testing mode
    with app.test_client() as client:
        yield client

def test_create_task(client):
    response = client.post('/tasks', json={'title': 'Test Task', 'description': 'Test Description'})
    assert response.status_code == 201  # Ensure the task is created successfully
    assert 'id' in response.json  # Ensure the response contains the new task ID

