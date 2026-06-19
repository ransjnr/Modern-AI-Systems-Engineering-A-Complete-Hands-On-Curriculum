# Project 3 — Medical Literature RAG System

Answer questions grounded in a small medical-literature corpus. Ships with an in-memory vector store so it runs with only an `OPENAI_API_KEY`. A Pinecone path is included as a comment.

> ⚠️ Educational/informational only — not medical advice.

## Run
```bash
pip install -r requirements.txt
cp ../../.env.example .env   # ensure OPENAI_API_KEY is set
python app/ingest.py        # embeds data/corpus.md into a local index
uvicorn app.main:app --reload
```
```bash
curl -X POST localhost:8000/ask -H 'Content-Type: application/json' \
  -d '{"question":"What lifestyle changes help lower blood pressure?"}'
```

## How it works
`ingest.py` chunks `data/corpus.md`, embeds each chunk, and saves vectors to `data/index.pkl`.
`rag.py` embeds the question, retrieves the top-k chunks by cosine similarity, and asks the LLM to answer **only** from that context (with citations).

## Tests
```bash
pytest -v
```
