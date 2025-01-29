import pytest
from VC_Radio_app import create_app
from VC_Radio_app.views.main_panel import main_panel_blueprint


@pytest.fixture
def client():
    app = create_app()
    app.testing = True  # Włączenie trybu testowego
    return app.test_client()

def test_app_creation():
    app = create_app()
    assert app is not None, "App instance should not be None"
    assert app.name == 'VC_Radio_app', "App name should match the module name"

def test_blueprint_registration():
    app = create_app()
    assert "main_panel" in app.blueprints, "Blueprint main_panel_blueprint should be registered"

def test_root_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200, "Root endpoint should return status code 200"
