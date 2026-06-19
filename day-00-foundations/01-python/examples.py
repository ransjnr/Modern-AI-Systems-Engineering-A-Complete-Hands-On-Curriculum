"""Runnable tour of the Python patterns used throughout the sprint."""
age: int = 25
price: float = 19.99
name: str = "Kwame"

scores = [92.3, 87.1, 95.8]
scores.append(88.5)
print("max:", max(scores), "| avg:", sum(scores) / len(scores))

config = {"model": "gpt-4o-mini", "temperature": 0}
print("model:", config.get("model", "default"))

doubled = [s * 2 for s in scores if s > 90]
print("doubled high scores:", doubled)

def predict_eta(distance_km: float, stops: int) -> float:
    return distance_km / 60 * 60 + stops * 20
print("eta:", predict_eta(12.5, 3))

class Counter:
    def __init__(self) -> None:
        self.n = 0
    def tick(self) -> int:
        self.n += 1
        return self.n
c = Counter()
print("ticks:", c.tick(), c.tick(), c.tick())

import json
parsed = json.loads('{"temperature": 0.2, "max_tokens": 100}')
print("parsed json:", parsed["temperature"])
