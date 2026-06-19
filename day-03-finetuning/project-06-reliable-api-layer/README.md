# Project 6 — Reliable Structured-Output API Layer

LLMs return free text by default; production systems need reliable, typed JSON.
This service uses OpenAI **function calling** + **Pydantic** validation + a **retry/repair**
loop so callers always get a valid object (or a clean error).

## Run
```bash
pip install -r requirements.txt
cp ../../.env.example .env   # OPENAI_API_KEY required
uvicorn app.main:app --reload
```
```bash
curl -X POST localhost:8000/extract -H 'Content-Type: application/json' \
  -d '{"text":"Customer Ama Mensah, +233201234567, wants a refund for order 8842 (faulty cable)."}'
```
Returns a validated `SupportTicket` with name, contact, order_id, category, and summary.

## Tests
```bash
pytest -v
```
