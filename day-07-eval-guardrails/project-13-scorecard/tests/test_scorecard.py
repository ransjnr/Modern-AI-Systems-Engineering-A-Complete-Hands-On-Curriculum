from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

def test_health():
    assert client.get("/health").json()["status"] == "ok"

def test_compare_flags_regression():
    base = {"n":4,"avg_similarity":0.90,"avg_judge":0.85,"avg_latency_s":1.0,"rows":[]}
    worse = {"n":4,"avg_similarity":0.80,"avg_judge":0.70,"avg_latency_s":1.2,"rows":[]}
    assert client.post("/compare", json={"baseline":base,"candidate":worse}).json()["regression"]

def test_compare_passes_when_stable():
    base = {"n":4,"avg_similarity":0.90,"avg_judge":0.85,"avg_latency_s":1.0,"rows":[]}
    same = {"n":4,"avg_similarity":0.91,"avg_judge":0.86,"avg_latency_s":1.0,"rows":[]}
    assert not client.post("/compare", json={"baseline":base,"candidate":same}).json()["regression"]
