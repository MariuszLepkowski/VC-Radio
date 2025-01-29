import pytest
from VC_Radio_app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.testing = True
    return app.test_client()

def test_root_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200, "Root endpoint should return status code 200"

def test_album_generator_endpoint(client):
    response = client.get('/album-generator')
    assert response.status_code == 200, "Album generator endpoint should return status code 200"

def test_about_endpoint(client):
    response = client.get('/about')
    assert response.status_code == 200, "About endpoint should return status code 200"

def test_links_endpoint(client):
    response = client.get('/links')
    assert response.status_code == 200, "Links endpoint should return status code 200"

def test_404_endpoint(client):
    response = client.get('/nonexistent-endpoint')
    assert response.status_code == 404, "Nonexistent endpoint should return status code 404"
