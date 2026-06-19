"""Retrieve top-k chunks and answer ONLY from them."""
import pickle
import numpy as np
from openai import OpenAI

client = OpenAI()
EMB_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4o-mini"

def _load():
    return pickle.load(open("data/index.pkl", "rb"))

def retrieve(question: str, k: int = 3) -> list[str]:
    index = _load()
    q = np.array(client.embeddings.create(model=EMB_MODEL, input=question).data[0].embedding)
    scored = [(float(np.dot(q, item["vec"]) /
               (np.linalg.norm(q) * np.linalg.norm(item["vec"]))), item["text"])
              for item in index]
    scored.sort(reverse=True)
    return [t for s, t in scored[:k] if s > 0.2]

def answer(question: str) -> dict:
    ctx = retrieve(question)
    if not ctx:
        return {"answer": "I don't have information on that in my sources.", "sources": []}
    context = "\n\n".join(f"[{i+1}] {c}" for i, c in enumerate(ctx))
    resp = client.chat.completions.create(
        model=CHAT_MODEL, temperature=0,
        messages=[{"role": "user", "content":
            "Answer using ONLY the context. Cite sources like [1]. If the answer is "
            f"not in the context, say you don't know.\n\nContext:\n{context}\n\n"
            f"Question: {question}"}])
    return {"answer": resp.choices[0].message.content, "sources": ctx}
