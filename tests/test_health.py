from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/api/v1/")

    assert response.status_code == 200
    assert "message" in response.json()


def test_health_endpoint():
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
