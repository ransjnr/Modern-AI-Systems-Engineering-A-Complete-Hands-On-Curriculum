"""Stage 1: generate/clean the raw dataset."""
from pathlib import Path
import numpy as np, pandas as pd, yaml

p = yaml.safe_load(open("params.yaml"))["prepare"]
rng = np.random.default_rng(p["seed"])
n = p["n_rows"]
df = pd.DataFrame({
    "distance_km": rng.uniform(0.5, 60, n).round(2),
    "num_stops": rng.integers(0, 12, n),
    "traffic": rng.integers(0, 3, n),
})
df["eta_minutes"] = (8 + 1.8 * df.distance_km + 6 * df.num_stops
                     + 3 * df.traffic + rng.normal(0, 5, n)).round(1)
Path("data").mkdir(exist_ok=True)
df.to_csv("data/prepared.csv", index=False)
print(f"prepared {len(df)} rows")
