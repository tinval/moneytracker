from fastapi.testclient import TestClient

from app.main import app

# We use TestClient to simulate requests to our FastAPI app
client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to MoneyTracker API"}


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
