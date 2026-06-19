# Project 16 — Resilient LLM Service

Wrap an LLM call in the full reliability stack: exact + semantic cache, per-client rate
limiting, retry with backoff, timeout, and a circuit-breaker fallback. Exposes `/metrics`
(cache-hit rate, p95 latency, fallback rate) and ships with load tests.

## Run
```bash
pip install -r requirements.txt
cp ../../.env.example .env     # OPENAI_API_KEY required
uvicorn app.service:app --reload --port 8013
```
```bash
curl -X POST localhost:8013/ask -H 'Content-Type: application/json' \
  -d '{"question":"What is a vector database?"}'   # repeat -> cache hit
curl localhost:8013/metrics
```

## Load test
```bash
# Option A: Locust UI
locust -f locustfile.py --host http://localhost:8013
# Option B: dependency-free async script
python scripts/loadtest.py
```

## Tests
```bash
pytest -v -m "not live"
```
