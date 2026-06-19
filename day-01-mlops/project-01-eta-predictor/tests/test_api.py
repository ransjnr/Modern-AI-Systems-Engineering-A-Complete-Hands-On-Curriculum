from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").json()["status"] == "ok"

def test_predict_requires_model_or_returns_value():
    r = client.post("/predict", json={"distance_km": 12.5, "num_stops": 3})
    # 200 if a model is trained, else 503 with a clear message
    assert r.status_code in (200, 503)
