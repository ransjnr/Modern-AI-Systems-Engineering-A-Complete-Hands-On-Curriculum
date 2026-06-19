"""Mock satellite database + orbital-mechanics calculator tools."""
import json, math
from langchain.tools import tool, StructuredTool
from pydantic import BaseModel, Field

SATELLITE_DB = {
    "iss": {"norad": 25544, "name": "International Space Station", "altitude_km": 420,
            "inclination_deg": 51.6, "operator": "NASA/Roscosmos/ESA/JAXA/CSA",
            "purpose": "crewed research station"},
    "hubble": {"norad": 20580, "name": "Hubble Space Telescope", "altitude_km": 547,
               "inclination_deg": 28.5, "operator": "NASA", "purpose": "optical/UV astronomy"},
    "starlink": {"norad": "many", "name": "Starlink Constellation", "altitude_km": 550,
                 "inclination_deg": 53, "operator": "SpaceX", "purpose": "broadband internet"},
}

@tool
def lookup_satellite_database(satellite_name: str) -> str:
    """Look up orbital and technical parameters for a satellite. Use FIRST when asked
    about any satellite. Supports ISS, Hubble, Starlink. Returns JSON."""
    key = satellite_name.lower().replace("-", "").replace(" ", "")
    for db_key, data in SATELLITE_DB.items():
        if db_key in key or key in db_key:
            return json.dumps(data, indent=2)
    return json.dumps({"error": f"'{satellite_name}' not found",
                       "available": list(SATELLITE_DB)})

class OrbitalInput(BaseModel):
    altitude_km: float = Field(..., description="Orbital altitude above Earth in km")

def _calc(altitude_km: float) -> str:
    R, mu = 6371.0, 398600.4418
    a = R + altitude_km
    period_min = round(2 * math.pi * math.sqrt(a ** 3 / mu) / 60, 2)
    v = round(math.sqrt(mu / a), 3)
    return json.dumps({"orbital_period_min": period_min, "orbital_velocity_kms": v,
                       "orbits_per_day": round(1440 / period_min, 2)})

calculate_orbital_params = StructuredTool.from_function(
    func=_calc, name="calculate_orbital_params",
    description="Compute orbital period/velocity from altitude. Use to verify orbit values.",
    args_schema=OrbitalInput)
