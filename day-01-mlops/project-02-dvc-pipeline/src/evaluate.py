"""Stage 3: train + score, emit DVC metrics."""
import json
from pathlib import Path
import pandas as pd, yaml
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

p = yaml.safe_load(open("params.yaml"))["train"]
df = pd.read_csv("data/features.csv")
X = df.drop(columns=["eta_minutes"]); y = df["eta_minutes"]
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=p["test_size"], random_state=42)
m = RandomForestRegressor(n_estimators=p["n_estimators"], max_depth=p["max_depth"],
                          random_state=42).fit(X_tr, y_tr)
pred = m.predict(X_te)
scores = {"mae": round(mean_absolute_error(y_te, pred), 3),
          "r2": round(r2_score(y_te, pred), 3)}
Path("metrics").mkdir(exist_ok=True)
json.dump(scores, open("metrics/scores.json", "w"), indent=2)
print("scores:", scores)
