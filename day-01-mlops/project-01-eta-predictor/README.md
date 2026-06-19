# Project 1 — Containerised ETA Predictor

Train a model that predicts package delivery time, wrap it in a FastAPI service, track training in MLflow, and package it in Docker.

## Run locally
```bash
poetry install
poetry run python scripts/generate_data.py      # creates data/raw/logistics_eta.csv
poetry run python scripts/train.py              # trains + logs to MLflow, saves model
poetry run uvicorn app.main:app --reload        # serves on :8000
```
Test it:
```bash
curl -X POST localhost:8000/predict -H 'Content-Type: application/json' \
  -d '{"distance_km": 12.5, "num_stops": 3, "traffic_level": "medium", "weather": "clear"}'
```

## Run with Docker
```bash
docker compose up --build      # API on :8000, MLflow UI on :5000
```

## MLflow
```bash
poetry run mlflow ui --port 5000   # then open http://localhost:5000
```

## Endpoints
- `GET /health` — liveness
- `POST /predict` — returns predicted ETA in minutes

## Tests
```bash
poetry run pytest -v
```
