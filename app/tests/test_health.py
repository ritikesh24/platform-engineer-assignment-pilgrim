from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "running"

def test_health(monkeypatch):
    class FakeConnection:
        def close(self):
            pass

    def fake_connect(**kwargs):
        return FakeConnection()

    monkeypatch.setattr(
        "app.main.psycopg2.connect",
        fake_connect
    )

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
