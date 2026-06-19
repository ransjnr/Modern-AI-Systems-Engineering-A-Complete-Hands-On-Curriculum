"""Reusable evaluators: similarity, LLM-as-judge, faithfulness proxy."""
import numpy as np
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

judge = ChatOpenAI(model="gpt-4o-mini", temperature=0)
emb = OpenAIEmbeddings(model="text-embedding-3-small")

def similarity(answer: str, reference: str) -> float:
    a, b = emb.embed_query(answer), emb.embed_query(reference)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def _score(prompt: str) -> float:
    out = judge.invoke(prompt).content
    digits = "".join(c for c in out if c.isdigit() or c == ".")
    try:
        return min(float(digits) / 10, 1.0)
    except ValueError:
        return 0.0

def judge_correctness(question: str, answer: str, reference: str) -> float:
    return _score("Grade the answer vs the reference for correctness/completeness. "
                  "Reply ONLY a number 0-10.\n"
                  f"Question: {question}\nReference: {reference}\nAnswer: {answer}\nScore:")

def faithfulness(answer: str, contexts: list[str]) -> float:
    ctx = "\n".join(contexts)
    return _score("Is the ANSWER supported by the CONTEXT? Reply ONLY 0-10 "
                  f"(10=grounded, 0=hallucinated).\nCONTEXT:\n{ctx}\nANSWER:\n{answer}\nScore:")
