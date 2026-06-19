"""Chunk the corpus, embed each chunk, and save a local vector index."""
import os, pickle, re
from pathlib import Path
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()
EMB_MODEL = "text-embedding-3-small"

def chunk(text: str, size: int = 400, overlap: int = 60) -> list[str]:
    words = text.split()
    out, i = [], 0
    while i < len(words):
        out.append(" ".join(words[i:i + size]))
        i += size - overlap
    return out

def main() -> None:
    text = Path("data/corpus.md").read_text()
    # split on headings, then chunk long sections
    sections = re.split(r"\n## ", text)
    chunks: list[str] = []
    for s in sections:
        chunks.extend(chunk(s.strip()))
    chunks = [c for c in chunks if len(c) > 40]
    vecs = client.embeddings.create(model=EMB_MODEL, input=chunks)
    index = [{"text": c, "vec": np.array(e.embedding)}
             for c, e in zip(chunks, vecs.data)]
    pickle.dump(index, open("data/index.pkl", "wb"))
    print(f"Indexed {len(index)} chunks -> data/index.pkl")

if __name__ == "__main__":
    main()
