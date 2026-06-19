import pickle
import numpy as np
from openai import OpenAI

client = OpenAI()

def recommend(interest: str, k: int = 3) -> list[dict]:
    products = pickle.load(open("data/index.pkl", "rb"))
    q = np.array(client.embeddings.create(
        model="text-embedding-3-small", input=interest).data[0].embedding)
    scored = []
    for p in products:
        v = p["vec"]
        cos = float(np.dot(q, v) / (np.linalg.norm(q) * np.linalg.norm(v)))
        scored.append((cos, p))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [{"id": p["id"], "name": p["name"], "score": round(s, 3)}
            for s, p in scored[:k]]
