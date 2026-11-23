import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_strong_password(client):
    response = client.post('/check_password', json={'password': 'Str0ng!Pass'})
    assert response.status_code == 200
    assert response.get_json()['strength'] == 'Очень надежный'

def test_weak_password(client):
    response = client.post('/check_password', json={'password': '123'})
    assert response.status_code == 200
    assert response.get_json()['strength'] == 'Слабый'

def test_common_password(client):
    response = client.post('/check_password', json={'password': 'password'})
    assert response.status_code == 200
    assert response.get_json()['score'] == 0
