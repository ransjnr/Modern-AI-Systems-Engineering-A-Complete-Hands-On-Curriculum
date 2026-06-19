import pytest
from pydantic import ValidationError
from app.schemas import ETARequest

def test_valid_request():
    r = ETARequest(distance_km=10, num_stops=2)
    assert r.traffic_level.value == "medium"

def test_rejects_negative_distance():
    with pytest.raises(ValidationError):
        ETARequest(distance_km=-1, num_stops=2)

def test_rejects_unknown_field():
    with pytest.raises(ValidationError):
        ETARequest(distance_km=10, num_stops=2, extra="nope")
