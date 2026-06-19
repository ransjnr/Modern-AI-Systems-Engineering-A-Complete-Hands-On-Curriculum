"""Create/ensure a small labelled QA dataset in LangSmith."""
from langsmith import Client

GOLDEN = [
    ("What is a vector database?",
     "A database that stores embeddings and supports similarity search."),
    ("What does RAG stand for?", "Retrieval-Augmented Generation."),
    ("What is LoRA used for?", "Parameter-efficient fine-tuning of LLMs."),
    ("Name one guardrail for LLM inputs.", "PII redaction or injection detection."),
]

def ensure_dataset(name: str = "day7-qa") -> str:
    client = Client()
    existing = [d for d in client.list_datasets() if d.name == name]
    ds = existing[0] if existing else client.create_dataset(name)
    if not existing:
        client.create_examples(
            inputs=[{"question": q} for q, _ in GOLDEN],
            outputs=[{"answer": a} for _, a in GOLDEN],
            dataset_id=ds.id)
    return ds.name
