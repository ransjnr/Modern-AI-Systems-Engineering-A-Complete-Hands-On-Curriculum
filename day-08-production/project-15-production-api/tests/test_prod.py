from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_health():
    assert client.get("/health").json()["status"] == "ok"

def test_ready_reports_checks():
    body = client.get("/ready").json()
    assert "checks" in body and "openai_key" in body["checks"]
