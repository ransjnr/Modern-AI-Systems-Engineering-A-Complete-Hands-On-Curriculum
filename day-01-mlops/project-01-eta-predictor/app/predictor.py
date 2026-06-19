"""Loads the trained pipeline and turns a request into a prediction."""
from pathlib import Path
import joblib
import pandas as pd
from app.schemas import ETARequest

MODEL_PATH = Path("models/eta_model_latest.joblib")
_TRAFFIC = {"low": 0, "medium": 1, "high": 2}
_WEATHER = {"clear": 0, "rain": 1, "storm": 2}


class Predictor:
    def __init__(self, model_path: Path = MODEL_PATH) -> None:
        if not model_path.exists():
            raise FileNotFoundError(
                f"Model not found at {model_path}. Run scripts/train.py first."
            )
        self.model = joblib.load(model_path)

    def predict(self, req: ETARequest) -> float:
        row = pd.DataFrame([{
            "distance_km": req.distance_km,
            "num_stops": req.num_stops,
            "traffic_level": _TRAFFIC[req.traffic_level.value],
            "weather": _WEATHER[req.weather.value],
        }])
        return float(self.model.predict(row)[0])
