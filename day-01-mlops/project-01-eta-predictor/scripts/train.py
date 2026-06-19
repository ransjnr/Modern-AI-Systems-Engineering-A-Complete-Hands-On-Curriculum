"""Train the ETA model and log the run to MLflow."""
import os
from pathlib import Path
import joblib
import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

FEATURES = ["distance_km", "num_stops", "traffic_level", "weather"]

def main() -> None:
    df = pd.read_csv("data/raw/logistics_eta.csv")
    X, y = df[FEATURES], df["eta_minutes"]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.2, random_state=42)

    params = {"n_estimators": 200, "learning_rate": 0.05, "max_depth": 4}
    mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI", "file:./mlruns"))
    mlflow.set_experiment("eta-predictor")
    with mlflow.start_run():
        model = GradientBoostingRegressor(random_state=42, **params).fit(X_tr, y_tr)
        pred = model.predict(X_te)
        mae, r2 = mean_absolute_error(y_te, pred), r2_score(y_te, pred)
        mlflow.log_params(params)
        mlflow.log_metrics({"mae": mae, "r2": r2})
        mlflow.sklearn.log_model(model, "model")
        Path("models").mkdir(exist_ok=True)
        joblib.dump(model, "models/eta_model_latest.joblib")
        print(f"MAE={mae:.2f} min  R2={r2:.3f}  -> models/eta_model_latest.joblib")

if __name__ == "__main__":
    main()
