"""Generate a synthetic logistics dataset."""
from pathlib import Path
import numpy as np
import pandas as pd

def main(n: int = 6000, seed: int = 42) -> None:
    rng = np.random.default_rng(seed)
    distance = rng.uniform(0.5, 60, n)
    stops = rng.integers(0, 12, n)
    traffic = rng.integers(0, 3, n)      # 0 low, 1 medium, 2 high
    weather = rng.integers(0, 3, n)      # 0 clear, 1 rain, 2 storm
    base = 8 + 1.8 * distance + 6 * stops
    base *= 1 + 0.15 * traffic + 0.1 * weather
    minutes = base + rng.normal(0, 5, n)
    df = pd.DataFrame({
        "distance_km": distance.round(2), "num_stops": stops,
        "traffic_level": traffic, "weather": weather,
        "eta_minutes": minutes.round(1),
    })
    out = Path("data/raw"); out.mkdir(parents=True, exist_ok=True)
    df.to_csv(out / "logistics_eta.csv", index=False)
    print(f"Wrote {len(df)} rows -> {out / 'logistics_eta.csv'}")

if __name__ == "__main__":
    main()
