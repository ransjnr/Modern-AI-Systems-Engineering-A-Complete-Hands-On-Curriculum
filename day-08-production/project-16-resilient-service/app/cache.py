"""Exact + semantic response cache."""
import hashlib
import numpy as np
from langchain_openai import OpenAIEmbeddings

emb = OpenAIEmbeddings(model="text-embedding-3-small")
_exact: dict[str, str] = {}
_semantic: list[tuple] = []          # (embedding, prompt, answer)
SIM_THRESHOLD = 0.95

def _key(p: str) -> str:
    return hashlib.sha256(p.strip().lower().encode()).hexdigest()

def lookup(prompt: str):
    k = _key(prompt)
    if k in _exact:
        return _exact[k], "exact"
    if _semantic:
        q = np.array(emb.embed_query(prompt))
        for vec, _p, ans in _semantic:
            cos = float(np.dot(q, vec) / (np.linalg.norm(q) * np.linalg.norm(vec)))
            if cos >= SIM_THRESHOLD:
                return ans, "semantic"
    return None, "miss"

def store(prompt: str, answer: str):
    _exact[_key(prompt)] = answer
    _semantic.append((np.array(emb.embed_query(prompt)), prompt, answer))
