"""Tiny in-memory RAG retriever (swap for your Day 2 vector store)."""
import numpy as np
from langchain_openai import OpenAIEmbeddings

emb = OpenAIEmbeddings(model="text-embedding-3-small")
DOCS = [
    "Refunds are issued within 5 business days to the original payment method.",
    "Our support hours are 9am-6pm GMT, Monday to Friday.",
    "To reset a password, use the 'Forgot password' link on the sign-in page.",
    "Enterprise plans include SSO, audit logs, and a dedicated success manager.",
]
_VECS = [np.array(emb.embed_query(d)) for d in DOCS]

def retrieve(query: str, k: int = 2) -> list[str]:
    q = np.array(emb.embed_query(query))
    sims = [(float(np.dot(q, v) / (np.linalg.norm(q) * np.linalg.norm(v))), d)
            for v, d in zip(_VECS, DOCS)]
    sims.sort(reverse=True)
    return [d for s, d in sims[:k] if s > 0.25]
