from app import app

def test_home_returns_application_details():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["application"] == "Flask CI/CD Demo"
    assert response.json["status"] == "Running"

def test_health_endpoint():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}

def test_ready_endpoint():
    response = app.test_client().get("/ready")
    assert response.status_code == 200
    assert response.json == {"status": "ready"}
