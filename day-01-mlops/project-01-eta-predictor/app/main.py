"""FastAPI service exposing the ETA predictor."""
from fastapi import FastAPI, HTTPException
from app.schemas import ETARequest, ETAResponse
from app.predictor import Predictor

app = FastAPI(title="ETA Predictor", version="1.0.0")

try:
    predictor: Predictor | None = Predictor()
except FileNotFoundError:
    predictor = None  # allow /health before the model is trained


@app.get("/health")
def health():
    return {"status": "ok", "model_loaded": predictor is not None}


@app.post("/predict", response_model=ETAResponse)
def predict(req: ETARequest):
    if predictor is None:
        raise HTTPException(503, "Model not loaded. Run scripts/train.py and restart.")
    minutes = predictor.predict(req)
    return ETAResponse(predicted_minutes=round(minutes, 1), distance_km=req.distance_km)
