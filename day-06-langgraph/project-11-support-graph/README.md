# Project 11 — Support Triage & Resolution Graph (LangGraph)

Classify → route (billing/technical/general) → loop back to clarify if vague → PAUSE for
human approval (`interrupt_before`) → finalise. Uses state, conditional routing, a bounded
cycle, memory, and human-in-the-loop.

## Run
```bash
pip install -r requirements.txt
cp ../../.env.example .env     # OPENAI_API_KEY required
uvicorn app.main:app --reload --port 8008
```
```bash
# 1) submit a ticket -> draft awaiting approval
curl -X POST localhost:8008/triage -H 'Content-Type: application/json' \
  -d '{"thread_id":"t1","message":"I was charged twice for my subscription."}'
# 2) approve -> finalise
curl -X POST localhost:8008/approve -H 'Content-Type: application/json' \
  -d '{"thread_id":"t1"}'
```

## Tests
```bash
pytest -v -m "not live"
```
