# Project 12 — Self-Correcting SQL Analyst (LangGraph)

Turn a plain-English question into SQL, run it against a seeded SQLite DB, and on error
**reflect and rewrite** the query (a bounded cycle) until it works. Read-only: only SELECT
is allowed. Checkpointed memory per `thread_id`.

## Run
```bash
pip install -r requirements.txt
cp ../../.env.example .env     # OPENAI_API_KEY required
uvicorn app.sql_main:app --reload --port 8009
```
```bash
curl -X POST localhost:8009/ask -H 'Content-Type: application/json' \
  -d '{"thread_id":"a1","question":"Total revenue per region, highest first?"}'
```

## Tests
```bash
pytest -v -m "not live"
```
