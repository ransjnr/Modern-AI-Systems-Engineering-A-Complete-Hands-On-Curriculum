"""Pydantic v2 models validating ETA prediction I/O."""
from enum import Enum
from pydantic import BaseModel, Field, computed_field


class TrafficLevel(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class Weather(str, Enum):
    clear = "clear"
    rain = "rain"
    storm = "storm"


class ETARequest(BaseModel):
    model_config = {"extra": "forbid"}  # reject unknown fields
    distance_km: float = Field(..., gt=0, le=500, description="Trip distance in km")
    num_stops: int = Field(..., ge=0, le=50, description="Number of stops")
    traffic_level: TrafficLevel = TrafficLevel.medium
    weather: Weather = Weather.clear


class ETAResponse(BaseModel):
    predicted_minutes: float
    distance_km: float

    @computed_field
    @property
    def predicted_hours(self) -> float:
        return round(self.predicted_minutes / 60, 2)
