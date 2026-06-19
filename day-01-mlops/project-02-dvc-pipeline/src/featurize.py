"""Stage 2: feature engineering."""
import pandas as pd, yaml
p = yaml.safe_load(open("params.yaml"))["featurize"]
df = pd.read_csv("data/prepared.csv")
df["stops_per_km"] = (df.num_stops / df.distance_km).round(3)
if p["scale"]:
    df["distance_km"] = (df.distance_km - df.distance_km.mean()) / df.distance_km.std()
df.to_csv("data/features.csv", index=False)
print("featurized ->", list(df.columns))
