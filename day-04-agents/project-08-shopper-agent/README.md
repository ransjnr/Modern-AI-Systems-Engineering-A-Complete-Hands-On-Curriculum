# Project 8 — eCommerce Smart Shopper Agent

A LangChain agent that takes a shopping query, uses **Tavily** to search the live web for
products and reviews, compares options with structured reasoning, and returns a ranked
recommendation with justification.

## Run
```bash
pip install -r requirements.txt
cp ../../.env.example .env     # OPENAI_API_KEY and TAVILY_API_KEY required
uvicorn app.main:app --reload  # :8005
```
```bash
curl -X POST localhost:8005/recommend -H 'Content-Type: application/json' \
  -d '{"query":"best wireless earbuds under $100"}'
```

## Bonus
- Cache identical queries to cut Tavily calls.
- Add a price-cap tool the agent must respect.
