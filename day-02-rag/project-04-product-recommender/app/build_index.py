"""Embed all products and save vectors for fast similarity search."""
import json, pickle
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def main() -> None:
    products = json.load(open("data/products.json"))
    texts = [f"{p['name']}: {p['desc']}" for p in products]
    embs = client.embeddings.create(model="text-embedding-3-small", input=texts)
    for p, e in zip(products, embs.data):
        p["vec"] = np.array(e.embedding)
    pickle.dump(products, open("data/index.pkl", "wb"))
    print(f"Indexed {len(products)} products")

if __name__ == "__main__":
    main()
