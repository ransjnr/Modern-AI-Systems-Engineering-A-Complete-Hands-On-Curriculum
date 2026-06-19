import json
from app.tools.satellite_tools import lookup_satellite_database, _calc

def test_lookup_known():
    assert "International Space Station" in lookup_satellite_database.run("ISS")

def test_lookup_unknown():
    assert "not found" in lookup_satellite_database.run("xyz123")

def test_orbital_calc():
    out = json.loads(_calc(420))
    assert out["orbital_period_min"] > 80 and out["orbits_per_day"] > 14
